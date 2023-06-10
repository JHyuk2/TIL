import numpy as np

a1_list = list(range(1, 10, 2))
a2_list = list(range(1, 9)) + list(range(4, 0, -1))

a1 = np.array(a1_list)
a2 = np.array(a2_list)
a2 = np.resize(a2, (3, 4))

# 1) a1 + a1
answer_1 = a1+a1
# print(answer_1)

# 2) a1 x 3
answer_2 = a1*3
# print(answer_2)

# 3) a3 = a2*4 
a3 = a2*4
# print(a3)

# 4) a2 * a3
print(a2 * a3)

# 5) a1의 평균 구하기
print(np.mean(a1))