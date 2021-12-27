# how to make bitwise combination & permutation
# 1st step: just using loop(for expression)

## --------- 1st. Using 'for' expression ----------
## 

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
# What if i want to make a list with at least one component? => just skip 0
## Bitwise examples
## print(1<<3) # 0001 => 1000
## print(3<<1) # 011 => 110 

## 2-1) powerset
## just using normal loop to powerset

## making error-1
# for i in range(1<<len(nums)):
#     print(f'i: {i} ', end='// ')
#     for j in range(i+1):
#         if i & (i<<j):
#             print(f'{nums[j]}', end=' ') 
#     print()

# 5, 10, 20 has also same result(1,0,1) tho...it's not true
# i = 5 # 101
# i = 10 # 1010 
# i = 20 # 10100

## Easist way to make powerset. just following binary mechanism
class Iterations:    
    def __init__(self):
        return
        
    def makePowerSet(self, items):
        for i in range(1<<len(items)):
            self.combo = []
            for j in range(len(items)):
                if (i >> j)%2 == 1:
                    self.combo.append(items[j])
            yield self.combo

    def powerSet(self, items:list) -> list:
        return list(self.makePowerSet(items))
    
    ## powerset will helps make combo and permutes easily.
    def combinations(self, items:list, length:int) -> list:
        powerset = self.powerSet(items)
        temp = []
        for ps in powerset:
            if len(ps) == length:
                temp.append(ps)
        return temp
    
    # arrangements of combinations
    def permutations(self, items:list, length:int) -> list:
        combos = self.combinations(items, length)
        for combo in combos:
            for components in combo:
                combo.pop(components)
        return

if __name__ == "__main__":
    nums = [16, 8, 4, 2, 1]
    tc = Iterations()
    # temp = tc.powerSet(nums)
    combos = tc.combinations(nums, 3)
    res = []
    for combo in combos:
        stack = []
        

    



# print(subsets)