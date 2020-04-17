from datetime import date

df = df[(df['column name'] > pd.Timestamp(date(2019,1,1)))]
df.head()