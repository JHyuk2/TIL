from collections import deque

def is_palindrome(char):
    d = deque()
    middle = len(char) //2 
    for c in char:
        d.append(c)
    for i in range(middle):
        if d.popleft() == d.pop():
            continue
        else:
            return False
    return True

# 실행문
char_list = ['eye', 'madam', 'radar', 'tomato']
for char in char_list:
    print(f"#is `{char}` palindrome? => {is_palindrome(char)}")
