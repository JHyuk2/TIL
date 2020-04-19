score = [88, 95, 70, 100, 99]
sum_tmp = 0
for s in score:
    sum_tmp += s
print('총점:', sum_tmp)
print('평균:', sum_tmp/len(score))

# ------------------ listslice ----------------
print('\n--------------listslice--------------')
nums = list(i for i in range(10))
print(nums[2:5])
print(nums[:4])
print(nums[6:])
print(nums[1:7:2])

# ------------------- listassign ----------------
print('\n--------------listassign--------------')
score = [88, 95, 70, 100, 99]
print(score[2])
score[2] = 55
print(score[2])

# -------------------- listreplace ----------------
print('\n--------------listreplace--------------')
nums = list(i for i in range(10))
nums[2:5] = [20, 30, 40]
print(nums)
nums[6:8] = [90, 91, 92, 93, 94]
print(nums)
nums[1:9] = [1]
print(nums)
# 신기하다...

# -------------------- dic ----------------
print('\n--------------dic--------------')
dic = {
    'boy':'소년',
    'school':'학교',
    'book':'책',
}
print(dic)

# -------------------- dicread ----------------
print('\n--------------dicread--------------')
# 위의 딕셔너리 사용
print(dic['boy'])
print(dic['book'])

# -------------------- dicget ----------------
print('\n--------------dicget--------------')
# 위의 딕셔너리 사용
print(dic.get('student'))
print(dic.get('student'), '사전에 없는 단어입니다.')
# 찾는 값이 없을때의 return값을 설정할 수 있다.

# -------------------- dicget ----------------
print('\n--------------dicget--------------')

if 'student' in dic:
    print('사전에 있는 단어입니다.')
else:
    print('이 단어는 사전에 없습니다.')

# -------------------- dicchange ----------------
print('\n--------------dicchange--------------')
dic['boy'] = '남자애'
dic['girl'] = '소녀' # 없는 값은 추가한다.
del dic['book']
print(dic)

# -------------------- dickeys ----------------
print('\n--------------dickeys--------------')
dic = {
    'boy':'소년',
    'school':'학교',
    'book':'책',
}
print(dic.keys()) # 키값만
print(dic.values()) # 밸류값만
print(dic.items()) #  둘 다