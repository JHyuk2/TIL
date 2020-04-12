import random
'''
equals 함수 만들기
'''

# setA = set(random.sample(range(1, 20), 10))
# setB = set(random.sample(range(1, 20), 10))
def eqauls(setA, setB):
    AandB = setA & setB
    AorB = setA | setB
    if AorB - AandB:
        return 'setA, setB는 같은 집합이 아닙니다.'
        
    else:
        return 'setA, setB는 같은 집합입니다.'

print('====원소는 콤마로 구분합니다.====')
setA = set(input('집합 A의 원소를 입력해주세요: ').split(','))
setB = set(input('집합 B의 원소를 입력해주세요: ').split(','))

# setA, setB
print('======setA,B========')
print(f'setA: {setA}')
print(f'setB: {setB}')
count = 0 

print(eqauls(setA, setB))