# Drug_Tweets_Classifier

- 1) 형태소 분석 o / x
- 2) 문장 일반화 o / x









## 1. 필요한 라이브러리 불러오기 

```python
#기본 라이브러리
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#전처리부분
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer

#모델부분
from sklearn import naive_bayes, svm
from sklearn.neighbors import KNeighborsClassifier

#검증부분 - Confusion_Matrix / Preciion and Reall
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score , recall_score , f1_score

#검증부분 - Cross Validation
from sklearn.model_selection import cross_val_score #점수 나타내기
```



## 2. Preprocessor

### 	1) 파일 읽고, text & label 선별 추출

```python
#파일을 읽고 필요한 정보 데이터만 가져오기
def read_file(file):
    data = pd.read_excel(file)
    text = data["text"]
    label = data['label']
    new_data = pd.DataFrame({"Text" : text,"Label" : label})
    return new_data
```

- <h6> 결과값 예시</h6>

> ```markdown
> #   data = read_file("data_sample.xlsx")
>   	print(data.head())
> 
> (Label)  					(Text)
> 1.0  사람들이 잘 모르는데 진짜 유명해졌으면 하는 일본 편의점 음식 #일본 #미니스톱 #...      
> 2.0  [#아이스의오락시간] #아이스 의 오락시간 \n과연 누가 아이스의 유연성 왕일지 얼...      
> 3.0  오. 오랫만에 #아이스 #돌체라떼 음 맛있겠다 (@ Starbucks in 부산광역...      
> 4.0  [맛집탐험대] 나를 놀라게한 커피 "TERAROSA" \n\n#TERAROSA #테...      
> 5.0  #로렉스 #아이스# 다이아#고씨쥬얼리#명품시계#금#화이트#골드#화이트골드 https...      
> 
> ```

###  	

###  	2) text를 단어별로 구분

```python
def split_all_sentence(text_data): # type(text_data) => DataFrame
    result = []
    count = 0
    for idx,text in enumerate(list(text_data)): # 수정 예정
        temp = text.split(sep = " ")
        result.append(temp)
    return result
```

- 코드 작성시 다음과 같이 바꿀 예정

  ~~for idx,text in enumerate(list(text_data)):~~

  **for text in list(text_data)**

  

- <h6> 결과값 예시</h6>

> ```markdown
> # print(split_all_sentence(data["Text"][:2]))
> 
> 
> [
> 	['사람들이', '잘', '모르는데', '진짜', '유명해졌으면', '하는', '일본', '편의점', '음식', '#일본', '#미니스톱', '#아이스', '#果実いちご氷', '세상사람들', '이것', '좀', '먹어보세요ㅠ유유ㅠㅠㅠ', '위에는', '달달한', '바닐라', '아이스고', '밑에는', '얼린', '딸기에', '연유가', '뿌려져', '있어요pic.twitter.com/KOERcUnoPR'],
>     
> 	['[#아이스의오락시간]', '#아이스', '의', '오락시간', '\n과연', '누가', '아이스의', '유연성', '왕일지', '얼른보러가요오\n\n링크\nhttps://youtu.be/CIrDBMGpi88\xa0']
> 	
> ]
> ```



### 	3) URL 제거

```python
#data에 있는 text 데이터에 대해 url 전부 제거
def remove_url(text_data):
    result = []
    for line in text_data: 
        new_line = []
        for text in line: # 단어별로 나눠진 텍스트들이 http, pic을 담고있다면 문장에서 제외
            if ("http" not in text) and ("pic" not in text):
                new_line.append(text) 
        result.append(new_line)
    return result
```

- <h6> 결과값 예시</h6>

> ```markdown
> # 	a = remove_url(split_all_sentence(data["Text"]))
>   	print (a)
> [['사람들이', '잘', '모르는데', '진짜', '유명해졌으면', '하는', '일본', '편의점', '음식', '#일본', '#미니스톱', '#아이스', '#果実いちご氷', '세상사람들', '이것', '좀', '먹어보세요ㅠ유유ㅠㅠㅠ', '위에는', '달달한', '바닐라', '아이스고', '밑에는', '얼린', '딸기에', '연유가', '뿌려져'], ['[#아이스의오락시간]', '#아이스', '의', '오락시간', '\n과연', '누가', '아이스의', '유연성', '왕일지']
> ```



	### 	4) 특수문자 / 숫자 제거

```python
#특수문자를 모두 제거하는 함수
def change(otl):
    result = []
    for line in otl:
        result_text = ""
        for word in line:
            if word.isalpha() : # 단어에 특문이 포함되지 않은 경우
                result_text += word
            else:
                for t in word: # 단어에 특문, 숫자가 포함된 경우 문자별로 파악
                    if t.isalpha():
                        result_text += t
                    else:
                        result_text += " " # 사라질 문자는 'space' 로 대체 => 5) 조정 필요
            result_text += " "
        result.append(result_text)
```

- <h6> 결과값 예시</h6>

> ```markdown
> # 	print(change([['#얼음활용법\n#얼음', '#아이스\n#생활꿀팁\n#경기도경제과학진흥원', '#GBSA\n\n집에', '보관해둔', '얼음을', '생활', '곳곳에서', '알뜰하게', '활용하는', '방법을']]))
> 
> [' 얼음활용법  얼음  아이스  생활꿀팁  경기도경제과학진흥원  GBSA  집에 보관해둔 얼음을 생활 곳곳에서 알뜰하게 활용하는 방법을 ']
> ```



	### 	5) 띄어쓰기 조정  <20. 01.19 함수화 수정>

-  띄어쓰기가 2칸 이상이면 한칸으로 조정

```python
def trim_spacing_word(changed_text):
    new_text = []
    for line in changed_text: # 한 줄씩 읽기.
        tmp = []
        for word in line.split(): # split(delimeter = whitespace) > default
            if word != " ":
                tmp.append(word)
        new_text.append(" ".join(tmp))
    print(new_text)
```

- <h6> 결과값 예시</h6>

> ```python
> # test = [' 얼음활용법  얼음  아이스  생활꿀팁  경기도경제과학진흥원  GBSA  집에 보관해둔 얼음을 생활 곳곳에서 알뜰하게 활용하는 방법을 ']
> 
> trim_spacing_word(test) 
> '''
> > ['얼음활용법 얼음 아이스 생활꿀팁 경기도경제과학진흥원 GBSA 집에 보관해둔 얼음을 생활 곳곳에서 알뜰하게 활용하는 방법을']
> '''
> ```



## 2 - 1) Preprocessor - Decompose(import hgtk, MeCab)

- 결과 도출 시 비교군으로 사용 할 것이므로, 각 과정에서 선택적으로 진행한다.



	### 	6) 형태소 추출

```python
#길이가 10 이상인 경우, 형태소 분석기로 나눠주는 함수
import MeCab

# custom_list = ["NNP","NNG","VV","VA","XR", "UNKNOWN"]
def kimchi(text, custom_list =  ["NNP","NNG","VV","VA","XR", "UNKNOWN"]):
    tagger = MeCab.Tagger()
    real = tagger.parse(text)
    separate_text = real.split()
    real_text = separate_text[:-1] # split된 마지막 요소엔 EOS 가 들어가서 잘라줘야함
    words = []
    types = []

    
    for i in range(len(real_text)):
        if i%2 == 0 :
            words.append(real_text[i])
        else:
            #istype = real_text[i].split(sep = ",")[0]
            types.append(real_text[i].split(sep = ",")[0])
            #if istype in custom_list :
                #types.append(real_text[i].split(sep = ",")[0])
    ans = list(zip(words,types))
    return ans
```

- <h6> 결과값 예시</h6>

> ```markdown
> # 	a = remove_url(split_all_sentence(data["Text"]))
>   	print (a)
> 
> ```



	### 	7) 자소 분리 & 한글만 보기

```python
## 각 음절에 맞게 자소를 꼴뚜기로 분리해준다.
import hgtk

a = hgtk.text.decompose("아이스")

print(a)
>> ㅇㅏᴥㅇㅣᴥㅅㅡᴥ 

print(a.replace("ᴥ",""))
>> ㅇㅏㅇㅣㅅㅡ
```

```python
## 함수로 나타냈을 때
import hgtk

def decompose_text(text_list):
    new_list = []
    for text in text_list:
        decomposed = hgtk.text.decompose(text)
        new_list.append(decomposed.replace("ᴥ",""))
    return new_list

## 영어, 한자, 일본어 등 제거
def remove_alpha(text_list):
    new_list = []
    alpha = "abcdefghijklmnopqrstuvwxyz"
    for text in text_list:
        one = ""
        for m in text.lower():
            if m not in alpha :
                one += m
        new_list.append(one)
    return new_list
```

- <h6> 결과값 예시</h6>

> ```markdown
> # 	test = ['사람들이 모르는게 good']
> 	after_decompose = decompose_text(test)
> 	after_remove = remove_alpha(after_decompose)	# 자소분리
>   	print (after_remove)						   	# 영어제거
>   
> ['ㅅㅏㄹㅏㅁㄷㅡㄹㅇㅣ ㅁㅗㄹㅡㄴㅡㄴㄱㅔ']
> ```





	### 	4) 입력대기중

```python

```

- <h6> 결과값 예시</h6>

> ```markdown
> # 	a = remove_url(split_all_sentence(data["Text"]))
>   	print (a)
> 
> ```

# 기타

은전한닢 프로젝트 구글 그룹스.

도움이 되는 정보들 찾아보면 있을지도?

https://groups.google.com/forum/#!topic/eunjeon/aNvCS72rloI