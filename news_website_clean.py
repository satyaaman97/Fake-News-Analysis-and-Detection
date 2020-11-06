import pandas as pd
import csv


# Work for news_sample.csv

# df_news_sample = pd.read_csv('News_sample/news_cleaned_2018_02_13.csv')#read in the news sample csv
df_news_sample = pd.read_csv('News_sample/xaa.csv', engine='python', encoding='utf-8', error_bad_lines=False, quoting=csv.QUOTE_NONE)
print(df_news_sample.head(1))


#create new df
#took off some of the the nan vcolumns
# id, url, content, title, keywords, tags, source
# dfnewssample = df_news_sample[['id','url','content','title','keywords','tags', 'source']].copy()
# df_news_sample.drop(columns=['inserted_at', 'updated_at', 'authors', 'meta_keywords', 'meta_description', 'summary'], axis =1)
del df_news_sample['inserted_at']
del df_news_sample['domain']
del df_news_sample['type']
del df_news_sample['updated_at']
del df_news_sample['scraped_at']
del df_news_sample['authors']
del df_news_sample['meta_keywords']
del df_news_sample['meta_description']
del df_news_sample['summary']

df_news_sample.to_csv(r'News_sample/news_sample_clean.csv', header=True) #this writes a new csv file to the folder.
print(df_news_sample.head(4))
print("===============================")
