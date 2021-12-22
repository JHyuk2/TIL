# how to make bitwise combination & permutation
# 1st step: just using loop(for expression)

## ------------ 1st. Using 'for' expression ----------
## 

nums = [1, 2, 3, 4]
permutes = []
combis = []

## 1) Permutation
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        permutes.append([i, j])

print(f'permutes: {permutes}')

## 2) Combination
for i in range(len(nums)):
    for j in range(len(nums)):
        combis.append([i, j])

print(f'combis: {combis}')