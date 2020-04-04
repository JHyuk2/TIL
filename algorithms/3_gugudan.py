# 9단 출력하기

# 1) for문 사용하기.
for i in range(1, 10):
    print(f'9*{i} = {9*i}')

# 2) while문 사용하기.
dan = int(input("원하는 단을 입력하세요: "))
i = 1

while i <= 9:
    print(f'{dan}*{i} = {dan*i}')
    i += 1