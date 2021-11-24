import random
# 시드설정을 통해 동일한 결과값을 받을 수 있다.
seed = random.seed(0)

numbers = []
for num in range(0, 10):
    numbers.append(random.randrange(0, 10))

print('생성된 리스트:', numbers)

for num in range(0, 10):
    if num not in numbers:
        print('%d 숫자는 리스트에 없네요.' %num)

num_list = random.sample(range(1, 10), 9)
print(num_list)