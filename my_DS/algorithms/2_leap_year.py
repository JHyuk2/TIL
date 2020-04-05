## 윤년
'''
year % 4 => 윤년
year % 100 => 평년
year % 400 => 윤년
'''

year = int(input("연도를 입력해주세요: "))

if ((year%4 == 0) and (year%100 != 0)) or (year%400==0):
    print(year,'년은 윤년입니다.')
else:
    print(year,'년은 윤년이 아닙니다.')

'''
    # 위와 같이 출력할 경우 띄어쓰기가 들어가기 때문에 다음으로 변경 가능하다.
    # 1) str(year) 으로 바꿔서 붙여주기 -> print(str(year) + '년은 윤년입니다.')
    # 2) print_format 사용하기 -> print(f'{year}년은 윤년입니다.')
'''