import pandas as pd
df = pd.read_csv("Salaries.csv")

#Q1
df.head(10)
df.head(20)
df.head(50)
df.tail()

#data types
df['salary'].dtype
df.dtypes

#groupby metthod
df_rank = df.groupby('rank')
df_rank.mean()
df.groupby('rank')[['salary']].mean()
df.groupby(['rank'],sort = False)[['salary']].mean()

#filtering
df_sub = df[df['salary'] > 120000]
df_f = df[df['sex'] == 'Female']

#Slicing
df['salary']
df[['rank','salary']]
df[10:20]

#method loc
df_sub.loc[10:20,['rank','sex','salary']]
df_sub.iloc[10:20,[0,3,4,5]]

#Sorting
df_sorted = df.sort_values(by = 'service')
df_sorted= df.sort_values( by=['service','salary'], ascending = [True,False])
df_sorted.head(10)
