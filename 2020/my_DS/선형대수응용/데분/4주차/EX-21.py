i, hap = 0, 0
num1, num2, num3 = 0, 0, 0

num1 = int(input('시작값: '))
num2 = int(input('끝값: '))
num3 = int(input('스텝: '))

for i in range(num1, num2+1, num3):
    hap += i

print(f'{num1}부터 {num2}까지 {num3}씩 증가한 값의 합 : {hap}')