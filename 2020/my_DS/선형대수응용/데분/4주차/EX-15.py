a = int(input("첫 번째 숫자: "))
ch = input('연산자 입력: ')
b = int(input('두 번째 숫자: '))

if ch == '+':
    print(f'{a} {ch} {b} =  {a + b}')
elif ch == '-':
    print(f'{a} {ch} {b} =  {a - b}')
elif ch == '*':
    print(f'{a} {ch} {b} =  {a * b}')
elif ch == '/':
    print(f'{a} {ch} {b} =  {a / b}')
elif ch == '//':
    print(f'{a} {ch} {b} =  {a // b}')
elif ch == '**':
    print(f'{a} {ch} {b} =  {a ** b}')
elif ch == '%':
    print(f'{a} {ch} {b} =  {a % b}')
else:
    print('알 수 없는 연산입니다.')