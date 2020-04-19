a = int(input('점수를 입력하세요: '))

if a%2 == 0:
    print("짝수입니다~")
else:
    print('홀수입니다~')

## 다른버전을 보면 아래
if a%2:
    print('홀수입니다~~')
else:
    print('짝수입니다~~')