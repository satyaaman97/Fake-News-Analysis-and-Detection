import pandas as pd


# Work for news_sample.csv

# df_news_sample = pd.read_csv('News_sample/news_cleaned_2018_02_13.csv')#read in the news sample csv
df_news_sample = pd.read_csv('News_sample/news_cleaned_2018_02_13.csv')
# print(df_news_sample.head())


#create new df
#took off some of the the nan vcolumns
# id, url, content, title, keywords, tags, source
dfnewssample = df_news_sample[['id','url','content','title','keywords','tags']].copy()
dfnewssample.to_csv(r'News_sample/news_sample_clean.csv', header=True) #this writes a new csv file to the folder. 
# print(dfnewssample.head(100))
print("===============================")
