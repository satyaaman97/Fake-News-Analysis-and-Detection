import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import re

from sklearn.model_selection import train_test_split

from gensim.models import Word2Vec

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, MaxPool1D, Dropout, Dense, GlobalMaxPooling1D, Embedding, Activation
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

def texts_to_sequences(titles, word_index):
    for title_arr in titles:
        for i in range(len(title_arr)):
            if title_arr[i] in word_index.keys():
                title_arr[i] = word_index[title_arr[i]]
            else:
                title_arr[i] = 0
    return titles

cb_df = pd.read_csv("./clickbait_data.csv")


t = [re.sub(r'\d', '', title) for title in cb_df["headline"]]
titles = [title.strip().lower().split() for title in t]

# print(titles[:2]) # [["should", "i", "get", "bings"], ['which', 'tv', 'female', 'friend', 'group', 'do', 'you', 'belong', 'in']]

w2vc_model = Word2Vec(titles, min_count=1, workers=4)
words = list(w2vc_model.wv.vocab)
# print(w2vc_model["should"]) # retrieve embeded vector of word "should"

word_freq = {}
for title_arr in titles:
    for word in title_arr:
        if word not in word_freq.keys():
            word_freq[word] = 1
        else:
            word_freq[word] += 1

word_freq = {k:v for k,v in word_freq.items() if v > 1}
sort_word_freq = sorted(word_freq.items(), key=lambda x:x[1], reverse=True)

word_index = {}
word_index['_PAD'] = 0
for i, item in enumerate(sort_word_freq):
    word_index[item[0]] = i+1

sequence = texts_to_sequences(titles, word_index)
inputs = pad_sequences(sequence)

labels = cb_df['clickbait']
X_train, X_test, y_train, y_test = train_test_split(np.array(inputs), labels, test_size=0.1,stratify=labels)

model = Sequential()
model.add(w2vc_model.wv.get_keras_embedding(True)) # .get_keras_embedding() Return a Keras 'Embedding' layer with weights set as the Word2Vec model's learned word embeddings
model.add(Dropout(0.2))
model.add(LSTM(100, return_sequences=True))
model.add(GlobalMaxPooling1D())
model.add(Dropout(0.2))
model.add(Dense(1))
model.add(Activation('sigmoid'))
model.summary()

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
history = model.fit(X_train, y_train, batch_size=32, validation_data=(X_test, y_test), epochs=3)

# model.save('clickbaitmodel2')

preds = [round(i[0]) for i in model.predict(X_test)]

print("================================Below is a test, similiar to what we are going to do with our data=================================================")

# test = ["Democrats Give Trump A Big F**ck You After He Attacks Them In Insane Twitter Rant", "Trumpsters Launch Insane Conspiracy Theory About The Boot On John McCain’s Foot",
#         "As U.S. budget fight looms, Republicans flip their fiscal script"]
# t = [re.sub(r'\d', '', title) for title in test]
# test_titles = [title.strip().lower().split() for title in t]
# test_inputs = pad_sequences(texts_to_sequences(test_titles, word_index))
#
# test_preds = [round(i[0]) for i in model.predict(test_inputs)]
# print(test_preds)


df = pd.read_csv("./Final_Dataset.csv")
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

my_titles = []
for title in df['title']:
    if not pd.isnull(title):
        title = re.sub(r'\d', '', title)
        title = title.strip().lower().split()
        my_titles.append(title)
    else:
        my_titles.append("")

my_inputs = pad_sequences(texts_to_sequences(my_titles, word_index))

clickbait_preds = [round(i[0]) for i in model.predict(my_inputs)]

df["Clickbait"] = clickbait_preds

df.to_csv("final_clickbait_dataset.csv", index=False, header=True)
