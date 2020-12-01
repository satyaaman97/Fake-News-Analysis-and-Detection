import numpy as np 
import pandas as pd 
import re 

from sklearn.model_selection import train_test_split

from gensim.models import Word2Vec

import tensorflow as tf 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, MaxPool1D, Dropout, Dense, GlobalMaxPooling1D, Embedding, Activation
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences

from sklearn import preprocessing
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split, KFold
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
import matplotlib
from matplotlib import pyplot as plt


print("All Libraries imported")

cb = pd.read_csv('clickbait/clickbait_data.csv')
print(cb.head(10))
print(cb.shape)

# cb the number of examples of each class
one = cb[cb['clickbait'] == '1'].shape[1]
zero = cb[cb['clickbait'] == '0'].shape[1]

# bar plot of the 3 classes
plt.bar(10,one,3, label="CB = 1")
plt.bar(15,zero,3, label="CB = 0")
plt.legend()
plt.ylabel('Number of examples')
plt.title('Propoertion of examples')
plt.show()