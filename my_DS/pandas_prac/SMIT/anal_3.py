import pandas as pd
import datetime
import os

# 체이닝 에러 끄기
pd.options.mode.chained_assignment = None  # default='warn'

def is_AM(data):
    return True if data == '오전' else False

def read_myexcel(file_location):
    # 파일 읽기
    data = pd.read_csv(file_location,
                            usecols = ['타임스탬프', '프로필 닉네임을 적어주세요.','1.  오늘의 기상 시각은?', '2. 오늘의 공부 시간은?', 
                            '3. 오늘 스터디 목표 달성도', '4. 개인 습관 달성 여부', '5. 오늘 본인의 학습 만족도'])
    data.columns =  ['date' , 's_name', 'wakeup_time', 'study_time', 'completion', 'habit', 'satisfaction']
    # 날짜 형식 맞추기
    dates = data['date']
    date_list = dates[0].split('/')
    year = int(date_list[0].strip())
    month = int(date_list[1].strip())
    day = int(date_list[2][:3].strip())
    d = datetime.date(year, month, day)
    data['date'] = [d] * data.shape[0]

    # 기상시각 
    wakeups = data['wakeup_time']
    for idx, w in enumerate(wakeups):
        waketime_list = w.split(':')
        h = int(waketime_list[0])
        m = int(waketime_list[1])
        w_time = datetime.time(hour = h, minute = m)
        data['wakeup_time'][idx] = w_time
    
    # 공부시간 - 실수형으로 변환
    s_times = data['study_time']
    tmp_s = pd.DataFrame()
    for idx, s_text in enumerate(s_times):
        tmp = ''
        if type(s_text) == int:
            s_text = str(s_text)
        for s in s_text:                
            if s.isdecimal():
                tmp += s
        # 길이가 홀수인 경우
        if len(tmp)%2 :
            if len(tmp) == 3:
                h = float(tmp[0])
                h += float(tmp[1:])/60
            # len == 1
            else:
                h = float(tmp[0])
        else:
            if len(tmp) == 4:
                h = float(tmp[0:2])
                h += float(tmp[2:])/60
                # len == 2
            else:
                h = float(tmp[0])
                h += float(tmp[1])/60
        if h >= 20:
            h /= 10
        data['study_time'][idx] = round(h, 1)

    # 플랜달성도, 만족도 -> 정수형으로 바꿔주기
    data['completion'].astype(int)
    data['satisfaction'].astype(int)
    return data


## 실제 실행문
# daily_0429 = read_myexcel('0429 Daily.csv')
# daily_0430 = read_myexcel('0430 Daily.csv')
# daily_0501 = read_myexcel('0501 Daily.csv')
# daily_0502 = read_myexcel('0502 Daily.csv')
# daily_0503 = read_myexcel('0503 Daily.csv')
# daily_0504 = read_myexcel('0504 Daily.csv')
# daily_0505 = read_myexcel('0505 Daily.csv')
# daily_0506 = read_myexcel('0505 Daily.csv')
# daily_0507 = read_myexcel('0505 Daily.csv')
# daily_0511 = read_myexcel('0511 Daily.csv')
daily_0512 = read_myexcel('0512 Daily.csv')
daily_0513 = read_myexcel('0513 Daily.csv')
daily_0514 = read_myexcel('0514 Daily.csv')
daily_0515 = read_myexcel('0515 Daily.csv')


# 데이터 연결
daily_list = pd.concat([daily_0512, daily_0513, daily_0514, daily_0515,])
daily_list = daily_list.sort_values(['s_name', 'date'], ascending = [False, True])

# 양식이 정리된 데이터로 변경
base_dir = 'C:\\Users\\win\\Hyuk2Coding\\TIL\\my_DS\\pandas_prac'
file_name = 'daily_list'
xlsx_dir = os.path.join(base_dir, file_name)

daily_list.to_csv('output_3기.csv', header = True, encoding = 'utf-8-sig', index=False)