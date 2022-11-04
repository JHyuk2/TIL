# part1. Counting/Frequency
# Q1. From data1.csv, calculate the frequency of the word "city"
# Q2. From data1.csv, calculate the frequency of the word "there"
# Q3. From data1.csv, calculate the frequency of the word ".".
# Q4. Compute the following: P(Will | I)

import csv
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

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
df_countwords = df_countwords.sort_values(by=['count'], ascending=False)
print(df_countwords.head(10))

# Part3. Histogram
# Q9. Plot the histogram of all the words occurred in Q6

# plt.plot(df_countwords['word'].values[:], df_countwords['count'].values[:])
# plt.xlabel("word")
# plt.ylabel("frequency")
# plt.show()

# Q10. Find top 10 bi-gram sequence
bigram_dict = {}
for line in df["contents"]:
    word_list = line.split(" ")
    if len(word_list) != 1:
        for idx in range(len(word_list)-1):
            temp = word_list[idx] + ' ' + word_list[idx+1]
            
            if temp not in bigram_dict.keys():
                bigram_dict[temp] = 1
            else:
                bigram_dict[temp] += 1


df_bigram = pd.DataFrame(list(bigram_dict.items()), columns=["word", "count"])
df_bigram = df_bigram.sort_values(by=['count'], ascending=False)
print(df_bigram.head(10))

# Q11. Plot the histogram of the two-words
# plt.plot(df_bigram['word'].values[:], df_bigram['count'].values[:])
# plt.xlabel("word")
# plt.ylabel("frequency")
# plt.show()

# Extra Credit 1: Find the top5 most frequently occurred four-word sequence
quadgram_dict = {}
for line in df["contents"]:
    word_list = line.split(" ")
    if len(word_list) > 3:
        for idx in range(len(word_list)-3):
            temp = " ".join([word_list[idx], word_list[idx+1], word_list[idx+2], word_list[idx+3]])
            
            if temp not in quadgram_dict.keys():
                quadgram_dict[temp] = 1
            else:
                quadgram_dict[temp] += 1

df_quadgram = pd.DataFrame(list(quadgram_dict.items()), columns=["word", "count"])
df_quadgram = df_quadgram.sort_values(by=['count'], ascending=False)
print(df_quadgram.head(5))