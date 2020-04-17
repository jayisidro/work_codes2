df['Goods/Services'] = df['column reference'].apply(lambda x: 'Services' if x > 70000000 else 'Goods')
df.head()