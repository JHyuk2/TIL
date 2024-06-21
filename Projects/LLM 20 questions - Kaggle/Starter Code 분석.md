# Starter Code 분석





### 1) 환경 설정 - Bash

```python
%%bash
cd /kaggle/working
pip install -q -U -t /kaggle/working/submission/lib immutabledict sentencepiece
git clone <https://github.com/google/gemma_pytorch.git> > /dev/null
mkdir /kaggle/working/submission/lib/gemma/
mv /kaggle/working/gemma_pytorch/gemma/* /kaggle/working/submission/lib/gemma/
```



```markdown
`%%bash`: Cell magic command, 현재 셀을 Bash창에서의 명령으로 실행함.
> 비슷한 기능을 하는 Line magic function
> - %bash: 현재 라인을 bash창에서 실행하게 한다.
> - !(명령어): 마찬가지로 Line magic command로, !pip install 등으로 사용 가능하다.

`pip install -options`: pip 설치를 위한 명령어와 옵션이다. 오픈소스에 있는 패키지를 가져옴
> pip install -h // pip --help 를 입력하면 어떤 옵션이 가능한지 볼 수 있다.
> -q(quiet): less give output, 출력메시지 적게띄우기
> -U(upgrade): 최신 버전이 있다면, 패키지를 업그레이드
> -t(target) <dir>: 목표 Directory에 패키지를 설치.
즉, `kaggle/working/submission/lib` 이라는 위치에 immutabledict, sentencepiece 패키지 설치

git clone <URL> > /dev/null
> `git clone <URL>`: 깃에 있는 레포를 현재 디렉토리로 가져오고 연결함.
> `/dev/null`: suppress output // 출력 억제

mkdir <dir>: 새로운 폴더 생성
mv <file dir> <target dir>: file dir에 있는 모든 것(*)을 target dir로 옮기기.
```



### 2) 환경 설정 - 코드 작성

```python
%%writefile submission/main.py # submission/main.py라는 파일로 코드를 작성함을 의미

# Setup
import os
import sys

# 제출을 위한 폴더생성
# submission path
KAGGLE_AGENT_PATH = "kaggle_siumlations/agent/" 

# 
if os.path.exists(KAGGLE_AGENT_PATH):
    sys.path.insert(0, os.path.join(KAGGLE_AGENT_PATH, 'lib'))
else:
    sys.path.insert(0, "/kaggle/working/submission/lib")
```

 `KAGGLE_AGENT_PATH` 경로가 존재하는지 확인하고, 존재하면 해당 경로의 `lib` 폴더를 파이썬 모듈 검색 경로에 추가합니다. 만약 해당 경로가 존재하지 않는다면, `/kaggle/working/submission/lib` 경로를 모듈 검색 경로에 추가합니다. 이는 특정 라이브러리를 우선적으로 로드하기 위한 설정입니다.



### 3) 환경 설정 - 라이브러리 불러오기

```python
# 왜 os, sys가 두 번이나 쓰였는지는 잘 모르겠다.
import contextlib
import os
import sys
from pathlib import Path

import torch
from gemma.config import get_config_for_7b, get_config_for_2b
from gemma.model import GemmaForCausalLM

if os.path.exists(KAGGLE_AGENT_PATH):
    WEIGHTS_PATH = os.path.join(KAGGLE_AGENT_PATH, "gemma/pytorch/7b-it-quant/2")
else:
    WEIGHTS_PATH = "/kaggle/input/gemma/pytorch/7b-it-quant/2"

```



### 4) class GemmaFormatter

```python
class GemmaFormatter:
    # 중요한 단어(대화의 시작과 끝을 알려주는 기호)
    _start_token = '<start_of_turn>'
    _end_token = '<end_of_turn>'

    # 
    def __init__(self, system_prompt: str = None, few_shot_examples: Iterable = None):
        self._system_prompt = system_prompt # 대화의 시작에 나타나는 첫 번째 메시지
        self._few_shot_examples = few_shot_examples # few shot learning sample
        
        # 사용자가 말할 때의 형식 정의
        self._turn_user = f"{self._start_token}user\n{{}}{self._end_token}\n" 
        # 모델(컴퓨터)이 말할 때의 형식 정의
        self._turn_model = f"{self._start_token}model\n{{}}{self._end_token}\n"
        self.reset() # 대화 상태 초기화 (아래에 reset 함수를 먼저 보고 돌아오자.)

    
    def __repr__(self):
        return self._state

    # 사용자와 모델함수 // 사용자가 말할 때와 모델이 말할 때 각각 호출된다.

    # 사용자가 말한 내용을 대화 상태에 추가
    def user(self, prompt):
        self._state += self._turn_user.format(prompt)
        return self
	# 모델이 말한 내용을 대화 상태에 추가.
    def model(self, prompt):
        self._state += self._turn_model.format(prompt)
        return self

    ## 대화 시작과 끝 함수.
    # 사용자의 대화 시작
    def start_user_turn(self): 
        self._state += f"{self._start_token}user\n"
        return self
	# 모델의 대화 시작
    def start_model_turn(self):
        self._state += f"{self._start_token}model\n"
        return self
	# 대화 끝
    def end_turn(self):
        self._state += f"{self._end_token}\n"
        return self

    # 리셋 함수 // 대화 상태를 초기화하는 함수
    def reset(self):
        self._state = "" # 대화 내용을 저장하는 변수
        
        # 만약 시스템 프롬프트가 있으면, 그것을 사용자 대화로 추가한다.
        if self._system_prompt is not None:
            self.user(self._system_prompt)
        # 예시 대화가 있으면, 그것을 추가한다.
        if self._few_shot_examples is not None:
            self.apply_turns(self._few_shot_examples, start_agent='user')
        return self

    # 대화 예시 적용!
    def apply_turns(self, turns: Iterable, start_agent: str):
        formatters = [self.model, self.user] if start_agent == 'model' else [self.user, self.model] # 대화의 주체에 따라 대화를 번갈아가며 추가할 함수를 정한다.
        formatters = itertools.cycle(formatters) # 대화가 번갈아가며 계속되게 해줌.
        for fmt, turn in zip(formatters, turns): # 주어진 대화 예시를 번갈아가며 추가.
            fmt(turn)
        return self

```

> _start_token, _end_token : 대화의 시작과 끝을 알려주는 특별한 표시.
>
> #### 최종적으로 이 클래스가 하는 일
>
> 이 클래스는 대화의 형식을 정의하고, 사용자가 말하거나 모델이 말할 때 대화 내용을 형식에 맞게 저장한다. 대화의 시작과 끝을 표시하고, 대화 예시를 쉽게 추가할 수 있도록 도와준다.
>
> - Example
>
> ```python
> formatter = GemmaFormatter(system_prompt="Hello, how can I help you today?")
> formatter.user("I need some information about my order.")
> formatter.model("Sure, can you please provide your order ID?")
> print(formatter)
> ```









```python
# Agent Definitions
import re


@contextlib.contextmanager
def _set_default_tensor_type(dtype: torch.dtype):
    """Set the default torch dtype to the given dtype."""
    torch.set_default_dtype(dtype)
    yield
    torch.set_default_dtype(torch.float)


class GemmaAgent:
    def __init__(self, variant='7b-it-quant', device='cuda:0', system_prompt=None, few_shot_examples=None):
        self._variant = variant
        self._device = torch.device(device)
        self.formatter = GemmaFormatter(system_prompt=system_prompt, few_shot_examples=few_shot_examples)

        print("Initializing model")
        model_config = get_config_for_2b() if "2b" in variant else get_config_for_7b()
        model_config.tokenizer = os.path.join(WEIGHTS_PATH, "tokenizer.model")
        model_config.quant = "quant" in variant

        with _set_default_tensor_type(model_config.get_dtype()):
            model = GemmaForCausalLM(model_config)
            ckpt_path = os.path.join(WEIGHTS_PATH , f'gemma-{variant}.ckpt')
            model.load_weights(ckpt_path)
            self.model = model.to(self._device).eval()

    def __call__(self, obs, *args):
        self._start_session(obs)
        prompt = str(self.formatter)
        response = self._call_llm(prompt)
        response = self._parse_response(response, obs)
        print(f"{response=}")
        return response

    def _start_session(self, obs: dict):
        raise NotImplementedError

    def _call_llm(self, prompt, max_new_tokens=32, **sampler_kwargs):
        if sampler_kwargs is None:
            sampler_kwargs = {
                'temperature': 0.01,
                'top_p': 0.1,
                'top_k': 1,
        }
        response = self.model.generate(
            prompt,
            device=self._device,
            output_len=max_new_tokens,
            **sampler_kwargs,
        )
        return response

    def _parse_keyword(self, response: str):
        match = re.search(r"(?<=\*\*)([^*]+)(?=\*\*)", response)
        if match is None:
            keyword = ''
        else:
            keyword = match.group().lower()
        return keyword

    def _parse_response(self, response: str, obs: dict):
        raise NotImplementedError


def interleave_unequal(x, y):
    return [
        item for pair in itertools.zip_longest(x, y) for item in pair if item is not None
    ]


class GemmaQuestionerAgent(GemmaAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _start_session(self, obs):
        self.formatter.reset()
        self.formatter.user("Let's play 20 Questions. You are playing the role of the Questioner.")
        turns = interleave_unequal(obs.questions, obs.answers)
        self.formatter.apply_turns(turns, start_agent='model')
        if obs.turnType == 'ask':
            self.formatter.user("Please ask a yes-or-no question.")
        elif obs.turnType == 'guess':
            self.formatter.user("Now guess the keyword. Surround your guess with double asterisks.")
        self.formatter.start_model_turn()

    def _parse_response(self, response: str, obs: dict):
        if obs.turnType == 'ask':
            match = re.search(".+?\?", response.replace('*', ''))
            if match is None:
                question = "Is it a person?"
            else:
                question = match.group()
            return question
        elif obs.turnType == 'guess':
            guess = self._parse_keyword(response)
            return guess
        else:
            raise ValueError("Unknown turn type:", obs.turnType)


class GemmaAnswererAgent(GemmaAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def _start_session(self, obs):
        self.formatter.reset()
        self.formatter.user(f"Let's play 20 Questions. You are playing the role of the Answerer. The keyword is {obs.keyword} in the category {obs.category}.")
        turns = interleave_unequal(obs.questions, obs.answers)
        self.formatter.apply_turns(turns, start_agent='user')
        self.formatter.user(f"The question is about the keyword {obs.keyword} in the category {obs.category}. Give yes-or-no answer and surround your answer with double asterisks, like **yes** or **no**.")
        self.formatter.start_model_turn()

    def _parse_response(self, response: str, obs: dict):
        answer = self._parse_keyword(response)
        return 'yes' if 'yes' in answer else 'no'


# Agent Creation
system_prompt = "You are an AI assistant designed to play the 20 Questions game. In this game, the Answerer thinks of a keyword and responds to yes-or-no questions by the Questioner. The keyword is a specific person, place, or thing."

few_shot_examples = [
    "Let's play 20 Questions. You are playing the role of the Questioner. Please ask your first question.",
    "Is it a person?", "**no**",
    "Is is a place?", "**yes**",
    "Is it a country?", "**yes** Now guess the keyword.",
    "**France**", "Correct!",
]


# **IMPORTANT:** Define agent as a global so you only have to load
# the agent you need. Loading both will likely lead to OOM.
agent = None


def get_agent(name: str):
    global agent
    
    if agent is None and name == 'questioner':
        agent = GemmaQuestionerAgent(
            device='cuda:0',
            system_prompt=system_prompt,
            few_shot_examples=few_shot_examples,
        )
    elif agent is None and name == 'answerer':
        agent = GemmaAnswererAgent(
            device='cuda:0',
            system_prompt=system_prompt,
            few_shot_examples=few_shot_examples,
        )
    assert agent is not None, "Agent not initialized."

    return agent


def agent_fn(obs, cfg):
    if obs.turnType == "ask":
        response = get_agent('questioner')(obs)
    elif obs.turnType == "guess":
        response = get_agent('questioner')(obs)
    elif obs.turnType == "answer":
        response = get_agent('answerer')(obs)
    if response is None or len(response) <= 1:
        return "yes"
    else:
        return response
```

