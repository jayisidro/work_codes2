df = pd.merge(df, other_df,  on='reference column', how='left')
df = df.drop_duplicates()
df.head()