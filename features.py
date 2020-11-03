import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import nltk
# from sklearn.preprocessing import LabelBinarizer
from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer
from wordcloud import WordCloud,STOPWORDS
# from nltk.stem import WordNetLemmatizer
# from nltk.tokenize import word_tokenize,sent_tokenize
from bs4 import BeautifulSoup
import re,string,unicodedata
# from keras.preprocessing import text, sequence
# from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
# from sklearn.model_selection import train_test_split
# from string import punctuation
# from nltk import pos_tag
# from nltk.corpus import wordnet
# import keras
# from keras.models import Sequential
# from keras.layers import Dense,Embedding,LSTM,Dropout
# from keras.callbacks import ReduceLROnPlateau
# import tensorflow as tf




def clean_data():
	# Work for news_sample.csv

	df_news_sample = pd.read_csv('news_sample.csv')#read in the news sample csv

	'''This is the cleaned data, took off as many NaN columns, but their is alot, each column and row is filled with some, so i took out the summary and tags
	and left the other ones.'''
	#create new df
	#took off some of the the nan vcolumns
	dfnewssample = df_news_sample[['id','domain','type','url','content','scraped_at','inserted_at','updated_at','title','authors','keywords','meta_keywords','meta_description']].copy()
	return dfnewssample


def strip_html(text):
    soup = BeautifulSoup(text, "html.parser")
    return soup.get_text()

#Removing the square brackets
def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)
# Removing URL's
def remove_between_square_brackets(text):
    return re.sub(r'http\S+', '', text)
#Removing the stopwords from text
def remove_stopwords(text):
    final_text = []
    for i in text.split():
        if i.strip().lower() not in stop:
            final_text.append(i.strip())
    return " ".join(final_text)

#Removing the noisy text
def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    text = remove_stopwords(text)
    return text

# def word_cloud(df):











if __name__ == "__main__":
	df_news_samples = clean_data()

	#Generate stopwords, ie. words that are common and don't add much interesting sentiment
	stop = set(stopwords.words('english'))
	punctuation = list(string.punctuation)
	stop.update(punctuation)

	#Apply denoise function on content column
	df_news_samples['content']=df_news_samples['content'].apply(denoise_text)

	print(str(df_news_samples.content.values))
	# print(df_news_samples.isna().sum())
	# print(df_news_samples.type.value_counts())

	plt.figure(figsize = (20,20)) # Text that is not Fake
	wc = WordCloud(max_words = 2000 , width = 1600 , height = 800 , stopwords = STOPWORDS).generate(str(df_news_samples.content.values))
	plt.imshow(wc , interpolation = 'bilinear')
	plt.savefig("wordcloud.png")







