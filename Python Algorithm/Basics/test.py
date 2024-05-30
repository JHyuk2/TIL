import random

# class Dice():
#     def __init__(self, num_sides, condition):
#         self.num_sides = num_sides
#         self.condition = condition

#     def roll(self):
#         score = random.randrange(self.num_sides) + 1
#         print("score:", score)
#         if not self.condition(score):
#             raise 1
#         return score
    

# even_dice = Dice(6, lambda x:x%2 == 0)

# try:
#     total_score = 0
#     for _ in range(3):
#         total_score += even_dice.roll()

#     print("Win!")
# except:
#     print('Lose')
# finally:
#     print("total_score:", total_score)

A = ["Mrs. smith"]
B = ['A153B']
import re

# mrs = re.compile(r'*.Mrs.*')
# print(mrs.search(A))
temp = [i for i in B[0]]
B = B[0].split(',')
print(B)