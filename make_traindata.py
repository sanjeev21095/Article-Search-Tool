# -*- coding: utf-8 -*-
"""
Created on Fri Oct 12 09:52:29 2018

@author: Sanjeev Narayanan
"""


import torch
import os
import re
import string
from nltk.corpus import stopwords
from stop_words import get_stop_words
import pandas as pd
from vectorize import vec
import numpy as np

### Add your path here #####

path = "C:/Users/Sanjeev Narayanan/Desktop/AJ Projects/Thesis Stuff/Task 5 - NLP/Main/outs/"

#############################

filenames = []
all_files = []
title = []
for i in os.listdir(path):
    filenames.append(path + '%s' %i)
    with open(path+'%s' %i,'r',encoding='utf-8') as myfile:
        data = myfile.read()
    data = re.sub(r'([^\s\w]|_)+', '', data)
    data = "".join(filter(lambda char: char in string.printable, data))
    all_files.append(data)
    title.append(i.replace('-',' ')[5:].title().split('.')[0])

stop_words = list(get_stop_words('en'))         #About 900 stopwords
nltk_words = list(stopwords.words('english')) #About 150 stopwords
stop_words.extend(nltk_words)

input_df = pd.DataFrame(all_files,columns = ['PaperText'])
input_df['Paper_text_new'] = input_df['PaperText'].apply(lambda x: ' '.join([word for word in x.split() if word not in (stop_words)]))
input_df['Paper_text_new'] = input_df['Paper_text_new'].str.split()

table1 = input_df.reset_index()['Paper_text_new'].values.tolist()
table1 = [x for x in table1 if len(x)>20]
title1 = []
for i,j in zip(table1,title):
    if len(i)>20:
        title1.append(j)

# reverse index titles
word_to_int = dict((w, i) for i, w in enumerate(title1))
int_to_word = dict((i, w) for i, w in enumerate(title1))

#call for getting vector of word

def choose_word(seq):
    vec_value = None
    while vec_value is None:
        try:
            num = np.random.randint(0,len(seq))
            str1 = seq[num]
            vec_value = vec(str1)
        except KeyError:
            continue

    return vec_value,str1

# Make X-train and Y-Train

row = []
new_row = []
outer = []
Y_data = []
count = 0
for i,m in zip(table1,title1):
    row = []
    for k in range(100):
        for j in range(4):
            word1,str1 = choose_word(i)
            #i = [x for x in i if x!=str1]
            row.append(word1)
            row_out = np.array(row)
        y_val = word_to_int[str(m)]
        Y_data.append(y_val)
    new_row.append(np.reshape(row_out,(100,4,50)))
    new_row_out = np.array(new_row)
#    count+=1
#    print(count)
Y_data = np.array(Y_data)
Y_data=np.reshape(Y_data,(40100,1))
X_data = np.reshape(new_row_out,(40100,4,50))    

a1 = np.zeros((40100,401))
for i in range(a1.shape[0]):
    for j in range(a1.shape[1]):
        if j == Y_data[i]:
            a1[i][j] = 1


import pickle

f = open('X_data.pckl', 'wb')
pickle.dump(X_data, f)
f.close()
f = open('Y_data_new_final.pckl', 'wb')
pickle.dump(a1, f)
f.close()

f = open('labels.pckl', 'wb')
pickle.dump(int_to_word, f)
f.close()

del Y_data,a1
def load_data():
    f = open('X_data.pckl', 'rb')
    X_data = pickle.load(f)
    f.close()
    f = open('Y_data.pckl', 'rb')
    Y_data = pickle.load(f)
    f.close()
    return X_data,Y_data