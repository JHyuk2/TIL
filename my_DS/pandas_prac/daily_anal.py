import pandas as pd
import datetime

def is_AM(data):
    return True if data == '오전' else False

def read_file(file_location):
    # 파일 읽기
    data = pd.read_excel(file_location,
        names = ['date', 's_name', 'wakeup_time', 'studied_time', 
                'completion','habit','staisfaction'],
        usecols=[0,1,2,3,4,5,6]
    )

    # 날짜 형식 맞추기
    dates = data['date']
    date_list = dates[0].split('.')
    year = int(date_list[0].strip())
    month = int(date_list[1].strip())
    day = int(date_list[2][:3].strip())
    d = datetime.date(year, month, day)
    data['date'] = [d] * data.shape[0]
    
    # 기상시각 
    wakeups = data['wakeup_time']
    for idx, w in enumerate(wakeups):
        waketime_list = w[3:].split(':')
        h = int(waketime_list[0])
        m = int(waketime_list[1])
        if not is_AM(w[:2]):
            h += 12
        w_time = datetime.time(hour = h, minute = m)
        # print(w_time)
        data['wakeup_time'][idx] = w_time
    
    # 공부시간 - 정수형으로 변환
    s_times = data['studied_time']
    for idx, s_text in enumerate(s_times):
        tmp = ''
        if type(s_text) == int:
            data['studied_time'][idx] = str(s_text)
            continue
        for s in s_text:                
            if s.isdecimal():
                tmp += s
        data['studied_time'][idx] =tmp
    print(data['studied_time'])
    
    return data

daily1 = read_file('0417 Daily.xlsx')
# print(daily1)
