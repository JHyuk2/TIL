
import csv
from telnetlib import WILL
import pandas as pd
import numpy as np

# open file and save as list
f = open("data1.csv", "r", encoding="utf-8")
rdr = csv.reader(f)

data_list = []

for line in rdr:
    data_list.append(",".join(line))
f.close()

# Q1~Q3) define find word function
def search(word, data):
    count = 0
    for line in data:
        count += line.count(word)
    
    return count

cities = search("city", data_list)
theres = search("there", data_list)
periods = search(".", data_list)

print("-------------------part1-------------------")
print(f'Q1) count of "city" : {cities}')
print(f'Q2) count of "there" : {theres}')
print(f'Q3) count of "." : {periods}')

# Q4) P(Will | I)
word1 = "will"
word2 = "I"

def get_probability(word, condition, data):
    temp = 0
    case = 0
    
    for line in data:
        if condition in line:
            case += 1
            if word in line:
                temp += 1
    return temp/case

prob = get_probability(word1, word2, data_list)
print(f'Q4) P(will | I) = {prob}')

# Part2. Data Cleaning and Frequency

print("\n-------------------part2-------------------")
# Q5. 1) remove all empty lines. 2) remove all digits/numbers except period (.)

## 5-1) remove all empty lines
df = pd.DataFrame(data_list, columns=["contents"])
print(f'before: {df.shape}')
df = df.drop(df[df["contents"]==""].index) 
print(f'after : {df.shape}')

## 5-2) remove all digits/numbers except period(.)
import re
def cleanText(text):
    return re.sub(r"[^a-zA-Z .]", '', text).strip()
    
df["contents"] = df["contents"].map(lambda x: cleanText(x))
print(df.head(), end='\n-----------------')



# Q6. Add the single space before  every peroid (".") so that period (".") can be considered as a word.

# def add_space(text):
#     return text.replace('.', ' .', text.count('.'))
def add_space(text):
    return re.sub("[.]", ' .', text)

df["contents"] = df["contents"].map(lambda x: add_space(x))
print(df.head())

# Q7. Find the total number of words after above text-processing step
# make dictionary and dict => dataframe
temp_dict = {}
for line in df["contents"]:
    word_list = line.split(' ')
    for word in word_list:
        if word not in temp_dict.keys():
            temp_dict[word] = 1
        else:
            temp_dict[word] += 1


print('-------------Q7 & Q8 ------------')
# Q7~8)
df_countwords = pd.DataFrame(list(temp_dict.items()), columns=["word", "count"])
print(df_countwords.sort_values(by=['count'], ascending=False).head(10))

# Part3. Histogram
print(df_countwords['word'].head(5).values[:])