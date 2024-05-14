# 2024.01.23



## SQL

#### Char vs VARCHAR

| SR.NO | CHAR                                                         | VARCHAR                                                      |
| ----- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1.    | CHAR datatype은 `고정된 길이` 의 문자를 저장하기 위해 사용된다. | VARCHAR datatype은 `가변 길이`의 문자를 저장하기 위해 사용된다. |
| 2.    | CHAR의 경우, 만약 입력된 문자의 길이가 설정된 길이보다 짧을 경우, 부족한 공간을 패딩하여 길이를 맞추기 위해 extra memory space를 사용한다. | VARCHAR의 경우, 만약 입력된 문자열의 길이가 설정된 길이보다 짧을 경우, extra memory space를 사용하지 않고 그냥 저장한다. |
| 3.    | CHAR는 "Character" 를 의미한다.                              | VARCHAR는 "Variable Character"를 의미한다.                   |
| 4.    | CHAR datatype의 저장 공간은 항상 n bytes로 동일하다.         | VARCHAR datatype의 저장 공간은 실제 입력된 문자들이 차지하고 있는 바이트의 합과 동일하다. |
| 5.    | 우리가 입력하려는 값이 같은 길이로 들어올 땐, CHAR를 사용해야 한다. | 우리가 입력하려는 값이 길이가 변할 수 있는 문자열인 경우, VARCHAR를 사용해야 한다. |
| 6.    | CHAR는 문자당 1바이트를 차지한다.                            | VARCHAR의 경우 기본적으로 문자당 1바이트를 사용하고, 길이 정보를 저장하기 위해 extra bytes를 사용하기도 한다. |
| 7.    | VARCHAR 보다 성능이 좋다.                                    | CHAR 에 비해 성능이 살짝 떨어진다.                           |

대략적으로 비교해 보면 이렇게 구분된다는 걸 알 수 있다.

근데, 그냥 메모리 그런거 모르겠고 쉽게 사용하고 싶으면 VARCHAR만 사용하면 그만인데, 왜 CHAR를 사용할까?



[MySQL Document에 나온 Char vs VarChar](https://dev.mysql.com/doc/refman/8.0/en/char.html)

> `CHAR` 와 `VARCHAR`는 비슷하지만, 저장과 값을 반환하는 과정에서 차이가 있다. (+ 최대 길이도.)
>
> - `CHAR`의 경우, 0~255자 사이의 값을 저장할 수 있다.
> - `VARCHAR`의 경우 0~65535자 사이의 값을 저장할 수 있다.



- HackerRank 문제를 보면, 아래와 같이 처리하는 과정으로 문제를 풀 수도 있는데,

  [문제 링크](https://www.hackerrank.com/challenges/the-blunder/problem?isFullScreen=false)

  `CAST(SALARY AS CHAR)` ,  `CAST(SALARY AS VARCHAR(10))` 이 두 가지를 써보면
  한 가지 경우에서 에러가 나는 것을 확인할 수 있다.



​	





