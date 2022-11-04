from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

# 1. Read .html file - scrapped chat file
page = open('html_chat/lck_20220328/page_1.html', 'rt', encoding='utf-8').read() # Read HTML and return char type
soup = BeautifulSoup(page, 'html.parser') # Soup 객체 생성

user_name = soup.select("body > li > a > span")
text_fragment = soup.select("body > li > span ")


# 2. Data Cleaning
# 2-1) Remove emoji

def demojize(bs4_text, user_name):
    """
    text_fragment[{even_number}] : timestamp
    text_fragment[{odd_number}] : ':" + text(emoji) + text(emoji)
    """
    
    demojized_text = []
    text = bs4_text[:] # deepcopy in depth level 1
    
    for idx in range(len(user_name)):
        cur_text = text[idx*2 + 1] # current_text
        res = '' 

        # (1) no emoji text
        if len(cur_text) == 2:
            demojized_text.append(cur_text.get_text()[2:])
            continue

        # (2) have emoji text
        for i, t in enumerate(cur_text):
            if i == 0:
                continue
            temp = t.get_text() + ' ' # if emoji ==> temp == ''
            res += temp
            res = " ".join(res.split()) # remove white space
        demojized_text.append(res)

    return demojized_text

chat_text = demojize(text_fragment, user_name)
user_name = list(map(lambda x:x.get_text(), user_name))

# Cleansing name & chat
print(user_name[0], chat_text[0])

# 3. Save data as DataFrame type
df = pd.DataFrame(list(zip(user_name, chat_text)),
                    columns=['User','Chat'])

# 3-1) Drop empty cells - only emoji text
print(df.shape)
print(f"empty cells: {len(df[df['Chat']==''])}")

df['Chat'].replace('', np.nan, inplace=True)
df.dropna(subset=['Chat'], inplace=True)
df.reset_index(drop=True, inplace=True)

print('------after remove-----')
print(df.shape)

# 4) Data Storage
df.to_csv("C:\\Users\\dm705\\Study\\TIL\\2022\\data_df_1.csv",
            sep=',',
            na_rep='')