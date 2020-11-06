import pandas as pd

df = pd.read_csv('../resized_v2.csv', usecols=['id','type','url','content','title','keywords','tags', 'source'])

# print(df.head(1))

df.to_csv('News_sample/news_sample_clean.csv', header=True)
print("Done")
