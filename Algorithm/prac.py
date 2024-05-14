# 1) 먼저 체를 이용하여 max_num 이하의 소수를 구하고
# 2) 두 수를 이루는 소수의 조합으로 표현
# 3) 공통되는 부분만큼 뽑아서 사용한다.

'''
ex) 
A = [2, 2, 3, 3]
B = [2, 3, 5]

# 공배수
count(2) => 2
count(3) => 2
count(5) => 1

2^2 * 3^2 * 5^1 -> 최소공배수

# 공약수
먼저 set(A|B) 로 둘을 묶어주고
각각 카운트에서 min값을 취함.
만약 겹치는 게 없을 경우 1 return
'''
def find_prime_num(max_num):
    # 0, 1번 인덱스는 0으로 처리한다.
    global prime
    length = max_num
    tmp = [0, 0] + [1] * length
    prime = []
    for idx, num in enumerate(tmp):
        if num == 1:
            prime.append(idx)
            n = 2
            while idx * n <= length:
                tmp[idx*n] = 0
                n += 1
    prime.pop()
    return prime

def solution(n, m):
    # n 이하의 소수 구함
    max_num = max(n, m)
    prime_list = find_prime_num(max_num)
    count_n = []
    count_m = []
    for p_num in prime_list:
        cnt_n = 0
        cnt_m = 0
        while not n % p_num:
            cnt_n += 1
            n //=p_num
        while not m % p_num:
            cnt_m += 1
            m //= p_num
        count_n.append(cnt_n)
        count_m.append(cnt_m)

    # 순서쌍 생성
    count_list = list(zip(count_n, count_m))
    min_list = list(map(min, count_list))
    max_list = list(map(max, count_list))

    # 최대공약수
    max_res = 1
    for idx, p_num in enumerate(prime_list):
        if min_list[idx]:
            max_res *= (p_num**min_list[idx])
    
    # 최소공배수
    min_res = 1
    for idx, p_num in enumerate(prime_list):
        if max_list[idx]:
            min_res *= (p_num**max_list[idx])

    return [max_res, min_res]