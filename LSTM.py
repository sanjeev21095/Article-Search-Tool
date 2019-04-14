# -*- coding: utf-8 -*-
"""
Created on Sat Oct 13 17:16:02 2018

@author: Sanjeev Narayanan
"""
import pickle

f = open('X_data.pckl', 'rb')
X_data = pickle.load(f)
f.close()
g = open('Y_data_new_final.pckl', 'rb')
Y_data = pickle.load(g)
f.close()


from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
from sklearn.utils import shuffle

X, y = shuffle(X_data, Y_data, random_state=0)

model = Sequential()
model.add(LSTM(256, input_shape=(X_data.shape[1], X_data.shape[2])))
model.add(Dropout(0.2))
model.add(Dense(Y_data.shape[1], activation='softmax'))
model.compile(loss='categorical_crossentropy', optimizer='adam')
print (model.summary())

model.fit(X, y, nb_epoch=100, batch_size=10)
model.save("my_model100_fin.h5")
