import pandas as pd

# 파일 불러오기
def read_file(file):
    data = pd.read_excel(file, sheet_name = '설문지 응답 시트1')
    name = data['1. 이름']
    wakeup_time = data['2. 기상시간']
    new_data = pd.DataFrame({'name':name, 'wakeup_time':wakeup_time})
    return new_data

# 시간데이터 입력받은거 다듬기
def time_trimmer(time_data):
    trim_hour = ['시','/','-']
    res = []
    for t in time_data:
        # 1) trimming
        t = t.replace(' ','')
        t.replace('분', '')
        for h in trim_hour:
            t = t.split(h)
        res.append(t)
    return res

data = read_file('test2.xlsx')
times = data['wakeup_time']
print(type(times))
for t in times:
    print(t)
# time_data = time_trimmer(data['wakeup_time'])
# print(time_data)
