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

# Path가 존재한다면 agent path + lib, 없다면 새로운 디렉토리 생성
if os.path.exists(KAGGLE_AGENT_PATH):
    sys.path.insert(0, os.path.join(KAGGLE_AGENT_PATH, 'lib'))
else:
    sys.path.insert(0, "/kaggle/working/submission/lib")
```

 `KAGGLE_AGENT_PATH` 경로가 존재하는지 확인하고, 존재하면 해당 경로의 `lib` 폴더를 파이썬 모듈 검색 경로에 추가합니다. 만약 해당 경로가 존재하지 않는다면, `/kaggle/working/submission/lib` 경로를 모듈 검색 경로에 추가합니다. 이는 특정 라이브러리를 우선적으로 로드하기 위한 설정입니다.



### 3) 