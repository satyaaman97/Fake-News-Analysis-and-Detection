import pandas as pd
import csv


# Work for news_sample.csv

# df_news_sample = pd.read_csv('News_sample/news_cleaned_2018_02_13.csv')#read in the news sample csv
df_news_sample = pd.read_csv('xaa.csv', engine='python', encoding='utf-8', error_bad_lines=False, quoting=csv.QUOTE_NONE)
# print(df_news_sample.head())


#create new df
#took off some of the the nan vcolumns
# id, url, content, title, keywords, tags, source
dfnewssample = df_news_sample[['id','url','content','title','keywords','tags', 'source']].copy()
dfnewssample.to_csv(r'news_sample_clean.csv', header=True) #this writes a new csv file to the folder.
# print(dfnewssample.head(100))
print("===============================")
