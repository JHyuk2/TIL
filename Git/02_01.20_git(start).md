# 1. 20 git

### How to 모내기

- 깃을 이용한 버전 관리. 그 첫걸음을 배워보자
- Source Code Management Tool => SCM이라고 부른다. _ What
- Version Control System _How



즉, 깃(git)이란

 ==> **소스 코드를 버전 분산을 통해 관리하는 것**

특정 폴더를 기점으로 관리하는 것.



### 깃을 시작하기에 앞서...

```bash
$ mkdir TIL ## TIL이란 폴더 생성
$ cd TIL 
$ git init ## 깃을 이렇게 하면 주소에 뭔가 이상하게 생긴다.
```

computer_name@DESKTOP MINGW64 ~/TIL **(master)**

- 갑자기 마스터라는 것이 생기는데, 이게 생기면 깃을 통해 관리하고 있다는 뜻.

```shell
$ rm -r .git/  ## 깃 버전관리를 취소하고 싶을 땐 remove를 통해 없애준다.
```

> 자 그럼 다시 init을 통해 깃을 사용해주자



### How to Start

​	1) 내 컴퓨터에서 저장하기

```bash
$ git status - 깃 상태정보를 보여줌, 변경정보를 보여줌!
$ git add - 변경된 파일을 commit(승인)하기 위한 준비가 된 상태.
--------------------------------------------------------
$ git config --global user.email "abc@gmail.com"
$ git config --global user.name "sooooftware"
$ git config --global --list # 변수설정 확인
------------------------------------------------------- meta data 설정
$ git commit -m "first commit"
$ touch a.txt

$ git log --oneline
$ git checkout master # 현재상태
```

​	2) 원격 저장소랑 연결하기

```bash
$ git remote add 저장소의 이름(별명) 저장소의 주소 
## git remote add origin https://github.com/JHyuk2/TIL.git (여기 마지막에 git 붙는거 잊지말자)
$ git remote -v  #더 보여줘!
$ git push origin master # 마지막으로 푸쉬를 넣으면 파일이 들어가게 된다.
```

- 여기 원격저장소의 네이밍이 굉장히 중요하다. 암묵적으로 첫 번째는 origin으로 네이밍한다.



```bash
순서대로 가보면
1) $ git init
2) $ git add ~
3) $ git 
```



이메일으

github.com/id/invitaions 들어가면 수락이 가능하다.

한 사람이 끝나야 가능한 경우 - Syncoronous 하다.

하지만 협업의 장점이 사라진다. 왜냐면 다른 사람들도 같이 작업해야하니까



fork and pull request



```bash
$ git credentail reject ## 인증 날리기
protocol=https
host=lab.ssafy.com
------------------------- # 새롭게 인증받을 준비 완료

```



