# lotto first place = [1, 3, 30, 33, 36, 39]
# bonus = 12

import random

# 1, 2, 3, 4, 5 place
count_list = [0 for _ in range(5)]
first_place = set([1, 3, 30, 33, 36, 39])
trial = 0
bonus = 12
while count_list[0] == 0:
    temp = set(random.sample(range(1, 46), 6))
    cnt = len(first_place & temp)
    trial += 1
    if cnt > 3:
        idx = -1*(cnt - 3)-1
        count_list[idx] +=1
        
print(count_list, trial)