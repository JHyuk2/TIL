select = int(input("1. 수식 계산기 / 2.두 수 사이의 합계 : "))


if select == 1:
    print('수식을 계산합니다.')
    numStr = input('*** 수식을 입력하세요 : ')
    answer = eval(numStr)
    print(f'{numStr}의 결과는 {answer}입니다.')

elif select == 2:
    print('두 수 사이의 합계를 구합니다.')
    answer = 0
    num1 = int(input('첫 번째 수: '))
    num2 = int(input('두 번째 수: '))
    for i in range(num1, num2+1):
        answer += + i
    print(f'{num1}부터 {num2}까지의 누적합은 {answer} 입니다.')
else:
    print("1 또는 2만 입력해야 합니다.")