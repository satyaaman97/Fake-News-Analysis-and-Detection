import pandas as pd


# Work for news_sample.csv

df_news_sample = pd.read_csv('news_sample.csv')#read in the news sample csv
# print(df_news_sample.head())


#create new df
#took off some of the the nan vcolumns
# id, url, content, title, keywords, tags, source
dfnewssample = df_news_sample[['id','url','content','title','keywords','tags']].copy()
dfnewssample.to_csv(r'news_sample_clean.csv', header=True)
print(dfnewssample.head(100))
print("===============================")


# Work for websites.csv
df_websites = pd.read_csv('websites.csv')#read in the website csv
print(df_websites.head())
print('')

#First type
df_type = df_websites[['url','type']].copy()#create new df
print(df_type.head())# this will print all data in the csv file with all types
df_type.to_csv(r'wtype_clean.csv', header=True)
print('')


df_type_fake = df_type[df_type['type'] == 'fake']# this will print only data with first type = fake
print(df_type_fake.head())
df_type_fake.to_csv(r'wtype_only_fake_news.csv', header=True)
print('')
# this prints everything but fake news in first type
df_type_notfake = df_type[df_type['type'] != 'fake']
df_type_notfake.to_csv(r'wnot_fake_news.csv', header=True)
print(df_type_notfake.head())

#Second type
df_2nd_type = df_websites[['url','2nd_type']].copy()

print(df_2nd_type.head())

print('')
# this will print only data with second type = fake
df_2nd_type_fake = df_2nd_type[df_2nd_type['2nd_type'] == 'fake']

print(df_2nd_type_fake.head())
df_2nd_type_fake.to_csv(r'w2nd_type_isfake_news.csv', header=True)

print('')
# this prints everything but fake news in second type
df_2nd_type_notfake = df_2nd_type[df_2nd_type['2nd_type'] != 'fake']
df_2nd_type_notfake.to_csv(r'w2nd_type_not_fake_news.csv', header=True)
print(df_2nd_type_notfake.head())

print('')
df_3rd_type = df_websites[['url','3rd_type']].copy()
print(df_3rd_type.head())
print('')
# this will print only data with second type = fake
df_3rd_type_fake = df_3rd_type[df_3rd_type['3rd_type'] == 'fake']

print(df_3rd_type_fake.head())
df_3rd_type_fake.to_csv(r'w3rd_type_is_fake_news.csv', header=True)
print('')
# this prints everything but fake news in second type
df_3rd_type_notfake = df_3rd_type[df_3rd_type['3rd_type'] != 'fake']
df_3rd_type_notfake.to_csv(r'w3rd_type_not_fake_news.csv', header=True)
print(df_3rd_type_notfake.head())
