# testcase
# 1. Russia - 3000 2700 2800 2200 2500 1900
# 2. Korea -  2800 2750 2995 1800 2600 2000
# 순서대로 정렬한 후에 비교해주면 되겠네...?ㅔ

'''
3
6
3000 2700 2800 2200 2500 1900
2800 2750 2995 1800 2600 2000
3
1 2 3
3 2 1
4
2 3 4 5
1 2 3 4
'''

from sys import stdin

C = int(input())
ans = [0] * C
size = []

for i in range(C):
    size.append(int(stdin.readline()))