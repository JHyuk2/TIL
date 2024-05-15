# GitHub 정리 - 1.21



## ~/TIL

```bash
$ git init
```

- .git  생성

---

###  ~/TIL/hw_ws

```bash
$ git init
```

- .git 또 생성

> ---
>
> ~/TIL
>
> ​	.git
>
> ​	/hw_ws/
>
> ​		.git
>
> ---

도식화하면 이렇게 되는데, 당연히 상위 `.git`의 명령어를 받아야하지만, 사실 그렇게 되지 않는다.

이를 해결하는 방법은 하위의  `.git`을 삭제하는 방법이 있음.



### jupyter file을 왜 굳이 복사해야 되는가?

사실 branch로 따로 관리하면 가능하긴 한데, 아직 잘 못다루기 때문에 pull 할 때 에러 뜰 수 있음.



### markdown으로 사진첨부 할 때 상대경로로 지정하는 방법!

- 사진 위치만 따로 정해서 `.`, `..`, `./폴더/파일` 이런 식으로 지정해주면 된다!

- typora에서 진행하고 vs code에서 



## jupyter-notebook, cmd에서 들어갈 때 번거로움을 줄여보자

### 1) git bash  - cd ~

- 홈 디렉토리로 나가기.

### 2) vi .bashrc

- vim 편집기를 열고 i(insert)를 누르면 편집 가능 상태가 된다.
- 참고로 vim에서 이동하는 키는 방향키가 아닌 `h,j,k,l`  이다.

### 3) alias jn = 'jupyter notebook'

- 주피터 노트북을 이제 jn으로 바꿔준 상태이다.
- vim편집기를 나오기 위해 esc를 세네번쯤 눌러보면 insert상태가 종료된다.

### 4) :wq - 저장하고 나오기

- w(write)의 약자
- q(quit)
- 위 두 개를 입력하고 엔터치면 나올 수 있다.

### 5) cat .bash_history

- 내가 쳤던 명령어들을 보여줌! 뭘 쳤는지 까먹었을 때 보자

### 6) ~(home)  => source ~/.bashrc

- 변경한 소스를 업데이트해준다. 저장한 .bashrc를 이제 사용할 수 있고 jupyter-notebook 대신 jn으로 호출!



## vim

vim 굉장히 더러운 에디터인데, 모든 키가 단축키라고 보면 된다.

`i(insert)` 대신 `o`를 누르면 한 줄 아래로 내려가서 입력모드가 된다.

~~빔을 외우기 위한 빔티커도 있다~~

친숙해지고 싶다면 `vim adventure`라는 게임을 해보자.



## Git 동시에 push하기

git push A && git push B

두 가지를 동시에 하면 되기 때문에, 마찬가지로 소스코드를 변경해주면 된다.

```bash
$ vi ~/.bashrc ## 먼저 home에서 실행해야한다.
```

```bash
alias jn='jupyter notebook'
alias ssafy='git push origin master && git push hub master'

:wq
------------------------------------------------------------
source ~/.bashrc
```

- 명령어창에 이제 `jn`만 입력하면 주피터가, `ssafy`를 입력하면 양쪽에 푸쉬가 된다!



### coding test_최대한 python스럽게 작성을 하는 게 더 좋다.

- 알고리즘 시험에서 가장 중요한 건 python 스타일을 많이 이용해보는 것.
- indexing / slicing & typecasting & list comprehension ...





<h4>어떻게 (=): 연산자</h4>
<h4>무엇을(데이터타입 == 자료형)</h4>
- 숫자
- 글자
- 부울

<h4>어디에(변수 / 컨테이너)  </h4>
	-  변수
	-  시퀀스형 자료 - string, tuple, list, range
	-  비시퀀스형 자료 - set, dictionary _ 중괄호`{}`를 사용하여 만듬



