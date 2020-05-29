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
                            usecols = ['타임스탬프', '이름을 알려주세요','1.  오늘의 기상 시각은?', '2. 오늘의 공부 시간은?', 
                            '3. 오늘 스터디 목표 달성도', '4. 개인 습관 달성 여부', '5. 오늘 본인의 학습 만족도'])
    data.columns =  ['date' , 's_name', 'wakeup_time', 'study_time', 'completion', 'habit', 'satisfaction']
    return data

data = read_myexcel('0501 Daily.csv')


# 기상시각 
wakeups = data['wakeup_time']
for idx, w in enumerate(wakeups):
    waketime_list = w.split(':')
    print(waketime_list)
    h = int(waketime_list[0])
    m = int(waketime_list[1])
    w_time = datetime.time(hour = h, minute = m)
    data['wakeup_time'][idx] = w_time

print(data.wakeup_time)