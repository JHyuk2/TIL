# Visualization Using Python #1

import pandas

# python ignore warnings
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

# visualize lib
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm # 시각화 내 폰트조절

# font to Notosans-KR
# 근데 지금은 NotoSans가 없어서 에러가 뜬다...
## > findfont; Font family 'NotoSansKR' not found error :(
fe = fm.FontEntry(fname='NotoSansKR-Regular.ttf', name='NotoSansKR')
fm.fontManager.ttflist.insert(0, fe)
plt.rc('font', family='NotoSansKR')

# figue, axes 생성
fig, ax = plt.subplots(dpi=150)

index = range(1, 6)
data = range(5, 0, -1)

# 라벨 설정하기
ax.set_title('연습')
ax.set_xlabel('인덱스')
ax.set_ylabel('데이터')

# 데이터 값 입력하기.
ax.plot(index, data)

# 하한가 등의 선을 정해서 보여줄 때.
plt.hlines(y=3, xmin=0, xmax=5, colors='red', linestyles="dotted")

# x축을 기준으로도 할 수 있음.
plt.vlines(x=3, ymin=0, ymax=5, colors='red', linestyles="dotted")

# 출력하기.
plt.show()