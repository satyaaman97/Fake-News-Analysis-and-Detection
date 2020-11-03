import pandas as pd


# Work for news_sample.csv

df_news_sample = pd.read_csv('news_sample.csv')#read in the news sample csv
print(df_news_sample.head())

'''This is the cleaned data, took off as many NaN columns, but their is alot, each column and row is filled with some, so i took out the summary and tags
and left the other ones.'''
#create new df
#took off some of the the nan vcolumns
dfnewssample = df_news_sample[['id','domain','type','url','content','scraped_at','inserted_at','updated_at','title','authors','keywords','meta_keywords','meta_description']].copy()
print(dfnewssample.head(100))
print("===============================")


# Work for websites.csv
#read in the website csv
df_websites = pd.read_csv('websites.csv')
print(df_websites.head())
print('')

'''This is the cleaned data, took off the NaN values, now it will just show the url and type'''
#create new df
#took off some of the the nan vcolumns
dfwebsites = df_websites[['url','type']].copy()
print(dfwebsites.head(1000))
