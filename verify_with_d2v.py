# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 16:47:59 2019

@author: Sanjeev Narayanan
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 11:37:51 2019

@author: Sanjeev Narayanan
"""

import os
import re
import string
from nltk.corpus import stopwords
from stop_words import get_stop_words
import pandas as pd


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


from gensim.models.doc2vec import Doc2Vec, TaggedDocument
from nltk.tokenize import word_tokenize

tagged_data = [TaggedDocument(words=word_tokenize(_d.lower()), tags=[str(i)]) for i, _d in enumerate(all_files)]

max_epochs = 100
vec_size = 50
alpha = 0.025

model = Doc2Vec(size=vec_size,alpha=alpha, min_alpha=0.00025,min_count=1,dm =1)
  
model.build_vocab(tagged_data)

for epoch in range(max_epochs):
    print('iteration {0}'.format(epoch))
    model.train(tagged_data,total_examples=model.corpus_count,epochs=model.iter)
    # decrease the learning rate
    model.alpha -= 0.0002
    # fix the learning rate, no decay
    model.min_alpha = model.alpha

model.save("d2v.model")
print("Model Saved")

path1 = "C:/Users/Sanjeev Narayanan/Desktop/AJ Projects/Thesis Stuff/Task 7 - D2V/"
model = Doc2Vec.load(path1+"d2v.model")

str1 = "Modeling the distribution of natural images is challenging, partly because of strong statistical dependencies which can extend over hundreds of pixels. Re-current neural networks have been successful in capturing "
test_data = word_tokenize(str1.lower())
v1 = model.infer_vector(test_data, steps=20, alpha=0.025)
similar_doc = model.docvecs.most_similar(positive=[v1])

out_docs = []
for i in similar_doc:
    out_docs.append(title[int(i[0])])
    
