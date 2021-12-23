# how to make bitwise combination & permutation
# 1st step: just using loop(for expression)

## --------- 1st. Using 'for' expression ----------
## 

nums = [1, 2, 3, 4]
# permutes = []
# combis = []

# ## 1) Permutations
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         permutes.append([i, j])

# print(f'permutes: {permutes}')

# ## 2) Combinations
# for i in range(len(nums)):
#     for j in range(len(nums)):
#         combis.append([i, j])

# print(f'combis: {combis}')


## ------ 2nd. Using bitwise shift operations ---------
# If i had a 4-length of number,
# The binary numbers are arranged in this order
# 00000 > 00001 > 00010 > 00011 ...
# What if i want to make a list with at least one component?


## Bitwise examples
## print(1<<3) # 0001 => 1000
## print(3<<1) # 011 => 110 


## 2-1) powerset
for i in range(1<<len(nums)):
    for j in range(i+1):
        if i & (i<<j):
            print(f'[i, i<<j]: [{i}, {i<<j}], {bin(i)}, {bin(i<<j)}', end=' ')
    print()

