# Chapter4 _Stack, 이종혁
opers = ['+', '-', '*', '/']
bracket = ['(', ')']

print('Question 1')
## 1-1) 중위 -> 후위
def postfix(data):
    oper_stack = []
    res = ''
    for i in data:
        if i not in (opers + bracket):
            res += i
        elif i == ')':
            while True:
                tmp = oper_stack.pop()
                if tmp == '(':
                    break
                res += tmp
        else:
            oper_stack.append(i)
    else:
        while oper_stack:
            res += oper_stack.pop()
    return res

## 1-2) 후위 -> 중위
def infix(data):
    num_stack = []
    res = ''
    for i in data:
        if i not in (opers + bracket):
            num_stack.append(i)
        else:
            # LIFO 이기 때문에 역순
            num2 = num_stack.pop()
            num1 = num_stack.pop()
            tmp = '(' + num1 + i + num2 + ')'
            num_stack.append(tmp)
    else:
        res = num_stack.pop()
    return res[1:-1] # 마지막 괄호 제거

# 실행문     
data1 = 'U*V*W+X-Y'
data2 = 'A+(B*C)-D/E'
data3 = 'ABC-D*+'
data4 = 'XYZ+AB-*-'
print(f'#1 {postfix(data1)}')
print(f'#2 {postfix(data2)}')
print(f'#3 {infix(data3)}')
print(f'#4 {infix(data4)}')

# 2) 괄호검사
print(' -------------------------------------  ')
print('Question 2')
tmp_data = 'a{b[(c+d)*e]-f}' # a, b 뒤에 곱하기 연산자가 생략되어있음.
opers = ['+', '-', '*', '/']
bracket_open = ['(', '[', '{']
bracket_close = [')', ']', '}']
# 가시성을 위해 oper_stack, num_stack으로 나누어 진행
oper_stack = []
num_stack = []

## 문제풀이
# i. 한글자씩 split
tmp_data = list(tmp_data)
# ii. 천천히 괄호 풀어주기.
counter = 0
for cur, i in enumerate(tmp_data):
    counter += 1
    if i not in (opers + bracket_open + bracket_close):
        num_stack.append(i)
    else:
        if i in bracket_close:
            idx = bracket_close.index(i)
            while True:
                tmp_res = ''
                tmp_oper = oper_stack.pop()
                if tmp_oper == bracket_open[idx]:
                    tmp_res = '(' + num_stack.pop() +')'
                    num_stack.append(tmp_res)
                    print(f'------ #{counter}--------')
                    print(f'num_stack: {num_stack}')    
                    print(f'oper_stack: {oper_stack}')
                    break
                else:
                    num2 = num_stack.pop()
                    num1 = num_stack.pop()
                    tmp_res = num1 + tmp_oper + num2
                    num_stack.append(tmp_res)
                    counter +=1 
                print(f'------ #{counter}--------')
                print(f'num_stack: {num_stack}')
                print(f'oper_stack: {oper_stack}')
        else:
            if i in bracket_open and tmp_data[cur-1].islower():
                oper_stack.append('*')
            oper_stack.append(i)

    print(f'------ #{counter}--------')
    print(f'num_stack: {num_stack}')
    print(f'oper_stack: {oper_stack}')
else:
    num2 = num_stack.pop()
    num1 = num_stack.pop()
    res = num1 + oper_stack.pop() + num2
    print(f'#result: {res}')

# 3) 스택에 남아있는 내용 적기.
print(' -------------------------------------  ')
print('Question 3')
values = []
for i in range(20):
    print(f'{i}', end=' ')
    if i % 3 == 0:
        values.append(i)
        print(values)
    elif i % 4 == 0:
        values.pop()
        print(values)

# 4) isPalindrome? _ 회문구하기
print(' -------------------------------------  ')
print('Question 4')

# 4-1) space제거 및 소문자변경
def preprocess(char):
    res = ''
    for c in char:
        if c.isalpha():
            res += c.lower()
    return res
# 4-2) 회문판독
def isPalindrome(char):
    middle = (len(char)+1)//2
    for i in range(middle):
        if char[i] != char[-i-1]:
            return False
    return True

# 실행문
input_list = ['eye', "madam, I'm Adam", 'race car', 'abba']
tmp_list = [None for _ in range(len(input_list))]
palindromes = [None for _ in range(len(input_list))]

for idx, i in enumerate(input_list):
    tmp = preprocess(i)
    tmp_list[idx] = tmp
    palindromes[idx] = isPalindrome(tmp)

print(tmp_list)
print(palindromes)

# 5) 프로그램이 하는 일
print(' -------------------------------------  ')
print('Question 5')

'''
십진법의 숫자를 이진법으로 나타내는 프로그램이다.
방법: 계속해서 2로 나누고, 나머지를 stack에 담아서 출력한다.

ex) 4096의 경우
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
이렇게 담기고, 이를 stack.pop()으로 나타낼경우,
12자리의 2진법 숫자로 표현할 수 있다. 
'''
s = []
n = 4096
while n > 0:
    s.append(n%2)
    n = n//2
    # print(n)
    # print(s)
while s:
    print(s.pop())
