# Starter Code 분석



## 1. 환경 설정

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



### 2) 환경 설정 - 모듈 임포트

```python
%%writefile submission/main.py # submission/main.py라는 파일로 코드를 작성함을 의미

# Setup
import os
import sys

# 제출을 위한 폴더생성
# submission path
KAGGLE_AGENT_PATH = "kaggle_siumlations/agent/" 

if os.path.exists(KAGGLE_AGENT_PATH):
    sys.path.insert(0, os.path.join(KAGGLE_AGENT_PATH, 'lib'))
else:
    sys.path.insert(0, "/kaggle/working/submission/lib")
```

>  `KAGGLE_AGENT_PATH` 경로가 존재하는지 확인하고, 존재하면 해당 경로의 `lib` 폴더를 파이썬 모듈 검색 경로에 추가한다. 
>
> 만약 해당 경로가 존재하지 않는다면, `/kaggle/working/submission/lib` 경로를 모듈 검색 경로에 추가한다. (특정 라이브러리를 우선적으로 불러오기 위함)



### 3) 환경 설정 - 모듈(라이브러리) 임포트

```python
# os, sys가 두 번이나 쓰였는지는 잘 모르겠다... 왜일까?
import contextlib
import os
import sys
from pathlib import Path

import torch
from gemma.config import get_config_for_7b, get_config_for_2b
from gemma.model import GemmaForCausalLM

# 이미 저장된 에이전트(7b)를 사용하기 위함인 것 같다.
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



## 2. main.py

물론, 환경설정부터 main.py에 작성되지만, 여기는 실제 작동을 위한 코드라고 보면 된다.



#### 1) 데코레이터와 컨텍스트 매니저

```python
# Agent Definitions
import re

@contextlib.contextmanager
def _set_default_tensor_type(dtype: torch.dtype):
    """Set the default torch dtype to the given dtype."""
    torch.set_default_dtype(dtype)
    yield
    torch.set_default_dtype(torch.float)
```



- ##### 한 줄씩 천천히 살펴보자.

```markdown
`import re` : 정규 표현식(Regural Expression)을 사용하기 위한 모듈 임포트

`@Contextlib.contextmanager` : 
- 데코레이터: 함수를 감싸서 추가적인 동작을 부여하는 함수
- 컨텍스트 매니저: `with`문과 함께 사용되면 특정 코드 블록의 시작과 끝에서 작업을 수행할 수 있도록 도와주는 객체
> 데코레이터는 나중에 조금 더 살펴보자.

`torch.set_defalut_dtype(dtype) ~ (torch.float)` : 컨텍스트 매니저가 기본 텐서 타입을 일시적으로 변경하고, 컨텍스트 블록이 끝난 이후에는 원래의 데이터 타입(torch.float)로 되돌리는 것을 의미한다.
```

- ##### 사용 예시

```python
with _set_default_tensor_type(torch.double):
    # 여기서 작성된 모든 텐서는 기본적으로 torch.double 타입을 사용한다.
    tensor = torch.tensor([1.0, 2.0, 3.0])
    print(tensor.dtype) # 출력 : torch.float64 (=torch.double, 64비트 부동 소수점 숫자)
    
# 컨텍스트 블록(with문)이 끝난 후 기본 dtype은 모두 float로 돌아간다. 
tensor = torch.tensor([1.0, 2.0, 3.0])
print(tensor.dtype) # 출력 : torch.float32 (= torch.float, 32비트 부동 소수점 숫자)
```

- ##### 왜 이렇게 사용하는가?

> 1. 정밀도 관리
>    - `torch.double`은 높은 정밀도를 제공하지만, 더 많은 메모리를 사용하고 계산 속도가 느려질 수 있다. 따라서 필요할 때만 double을 사용하는 것이 더 효율적이다.
> 2. 코드 가독성
>    - 컨텍스트 매니저를 사용하면, 코드의 특정 부분에서만 데이터 타입이 변경된다는 것을 명시할 수 있게 된다!
>
> 
>
> 즉, 특정 연산에서 더 높은 정밀도를 확보할 수 있으며, 코드의 다른 부분에 영향을 주지 않고 데이터 타입을 관리할 수 있기 때문에 데코레이터로 사용하게 되는 것이다.



#### 2) Gemma Agent

```python
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
```



- ##### `__init__` 메서드 : 클래스 정의 및 초기화

```markdown
#### 1) `__init__` : 객체 생성과 함께 자동으로 호출되는 메서드
- `variant`, `device`, `system_prompt`, `few_shot_examples` 인자를 입력받아서 실행
- `self._variant`, `self._device`는 클래스의 '인스턴스 변수'로서 저장
- `GemmaFormatter` 객체를 생성하여 `self.formatter`에 저장한다.

> 변수명에 `_`를 붙이는 관례  
> 1. 단일 언더바(`_`)
> - 해당 속성이나 메서드가 **내부 사용용** 임을 암시한다.
> - 실제로 접근을 막지는 않지만, 해당 속성이나 메서드가 클래스 외부에서 직접 접근하면 안 된다는 신호
> 2. 이중 언더바(`__`) <`name mangling`>
> 클래스 정의 내부에서 변수명을 고유하게 만들어 서브클래스에서 `같은 이름의 변수가 충돌하는 것을 방지`

#### 2) `model_config` : 모델 초기화
- `get_config_for_2b()` or `get_config_for_7b()` 함수를 호출하여 모델 설정을 가져온다.
- 토크나이저 경로와 양자화(quant)여부를 결정.

#### 3) `with`문 : 컨텍스트 매니저를 통한 인스턴스 모델 생성
- 데이터 타입을 설정한 후 모델을 초기화
- 체크포인트로부터 가중치 로드
- 모델을 지정된 장치(`cuda:0`) 로 이동시키고, 평가 모드(`eval()`)로 설정한다.
```

- ##### 사용 예시

```python
# 객체 생성 (__init__ 호출)
Agent = GemmaAgent() 
```



- ##### `__call__` 메서드 : 클래스 호출

```python
	def __call__(self, obs, *args):
        self._start_session(obs)
        prompt = str(self.formatter)
        response = self._call_llm(prompt)
        response = self._parse_response(response, obs)
        print(f"{response=}")
        return response
```

- `__call__` 메서드 : 객체가 호출될 때 실행

  > `obs`와 추가 인자를 받는다.
  >
  > `_start_session`메서드를 호출하여 세션을 실행한다.
  >
  > `formatter` 객체를 문자열로 변환하여 prompt 생성
  >
  > `_call_llm` 메서드를 호출하여 언어 모델의 응답 받기.
  >
  > `_parse_response` 메서드를 호출하여 응답을 파싱



- ##### `_start_session` 메서드 : 세션 시작 

```python
    def _start_session(self, obs: dict):
        raise NotImplementedError
```

- 세션을 시작하는 메서드로, 구체적인 구현은 서브클래스에서 제공되어야 한다.
  - `NotImplementedError`를 발생시켜 서브클래스에서 구현해야 함을 명시!



- ##### `_call_llm` 메서드: 언어 모델 호출

```python
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
```

- LLM 언어 모델을 호출하는 메서드이다.

  > - `prompt`, `max_new_tokens` 및 기타 샘플러 매개변수를 받는다.
  >
  > - `sampler_kwargs`(=하이퍼 파라미터)가 제공되지 않으면 기본 값을 설정한다.
  > - 모델의 `generate` 메서드를 호출하여 응답을 제공한다.
  > - 생성된 응답을 반환한다.



- ##### `_parse_keyword` 메서드 : 키워드 파싱

```python
    def _parse_keyword(self, response: str):
        match = re.search(r"(?<=\*\*)([^*]+)(?=\*\*)", response)
        if match is None:
            keyword = ''
        else:
            keyword = match.group().lower()
        return keyword
```

- 정규 표현식을 사용하여 두 개의 응답(`**`) 사이에서 텍스트를 찾는 메서드이다.

  - 매치가 없으면 빈 문자열을 반환하고, 매치가 있으면 키워드를 소문자로 변환하여 전달한다.

  > **정규표현식**
  >
  > ```python
  > r"(?<=\*\*)([^*]+)(?=\*\*)"
  > ```
  >
  > 이 정규표현식은 두 개의 별표(`**`)로 둘러싸인 단어를 찾는 데 사용된다.
  >
  > - `r`: 문자열 앞에 붙는 `r`은 `raw string`의 약자로, 이스케이프 문자를 무시하고 백슬래시(`\`)를 일반 문자로 처리한다.
  > - `(?<=\*\*)` : 긍정형 후방탐색(Positive Lookbehind). `**` 가 앞에 있는 단어를 찾는다.
  >   - `(?<= ...`) : `...` 부분이 앞에 있어야 함을 의미
  >   - `\*` : 정규표현식에서 문자 그대로를 인식하기 위해 이스케이프 문자(백슬래시)로 사용해야 한다.
  > - `([^*]+`) : 별표가 아닌 하나 이상의 문자.
  >   - [`^ ...]` : 대괄호 안의 `^`는 부정을 의미한다. 여기서는 별표(`*`)를 제외한 모든 문자를 의미한다.
  >   - `+` : 앞의 패턴이 한 번 이상 반복됨을 의미한다.
  > - `(?=\*\*)` : 긍정형 전방탐색(Positive Lookahead). `**` 가 뒤에 있는 부분을 찾는다.
  >   - `(?= ...)` : `...` 부분이 뒤에 있어야 함을 의미한다.
  >
  > ```python
  > # Regex example
  > response = "The keyword is **example** in this sentence."
  > match = re.search(r"(?<=\*\*)([^*]+)(?=\*\*)", response)
  > if match:
  >     keyword = match.group()
  >     print(keyword)  # 출력: example
  > ```





```python


    def _parse_response(self, response: str, obs: dict):
        raise NotImplementedError
        
        
    def interleave_unequal(x, y):
        return [
            item for pair in itertools.zip_longest(x, y) for item in pair if item is not None
        ]
```





```markdown

```











```python
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

LLM learning/Fine tuning(`Few shot learning`)에 대한 이해가 조금 더 필요할 거 같다.





---

### RAG pipeline

Query Expansion - Retrieval - Reranker - Passage Filter - Passage compressor - Prompt maker - Generator(LLM)

- 어떻게 답변을 내놓는지에 대한 이해가 필요할 것 같다.
- langchain? huggingface?





박결님 아이디어 // decision tree의 entropy 개념을 활용하면 '질문'에 대한 평가도 가능하지 않을까?

+ 단어마다 vector값 계산(cosine sim)을 통해 가까운 카테고리를 구축한 후, feature를 골라내는 방법은...?

수용님 아이디어 // 데이터셋을 구축해서 시나리오를 짜보는 것도 가능할 것 같다.

> 일단 학습 데이터셋에서 수작업으로 category를 추가하고 나눠보는건...?
>
> example. 

