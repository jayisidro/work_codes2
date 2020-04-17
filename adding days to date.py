from datetime import timedelta  

df.loc[(df['Currency'] == 'USD') | (df['Goods/Services'] == 'Goods'), 'Target PO Date'] =  df['PR Creation Date'] +  timedelta(days=52) 
df.loc[(df['Currency'] != 'USD') & (df['Goods/Services'] != 'Goods'), 'Target PO Date'] =  df['PR Creation Date'] +  timedelta(days=135) 
df.loc[(df['Currency'] == 'USD') | (df['Goods/Services'] == 'Services'), 'Target PO Date'] =  df['PR Creation Date'] +  timedelta(days=52) 
df.loc[(df['Currency'] != 'USD') & (df['Goods/Services'] != 'Services'), 'Target PO Date'] =  df['PR Creation Date'] +  timedelta(days=109) 

df.head()