score = int(input('점수 입력: '))

if score >= 900:
    print('A')
else :
    if score >= 800:
        print('B')
    else:
        if score >= 700:
            print('c')
        else:
            if score >= 600:
                print('d')
            else:
                print('F')

print('학점입니다... ^^')