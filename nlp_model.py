import pandas as pd
import numpy as np

#library for stop words
from nltk.corpus import stopwords 


df = pd.read_csv('clickbait/clickbait_data.csv')

df.head()
df.info()

x_data= df['title']+ " " + df['content']
y_data= df['type']

x_data[:1000]

stop = stopwords.words('english')

print(x_data)