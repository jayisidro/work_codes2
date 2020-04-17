df.loc[(df['Approved Date'] >= pd.Timestamp(date(2020,1,1))) & (df['Approved Date'] <= pd.Timestamp(date(2020,1,31))), 'column_name'] =  'Tag 1'
df.loc[(df['Approved Date'] >= pd.Timestamp(date(2020,2,1))) & (df['Approved Date'] <= pd.Timestamp(date(2020,2,18))), 'column_name'] =  'Tag 2'
df.loc[(df['Approved Date'] >= pd.Timestamp(date(2020,2,19))) & (df['Approved Date'] <= pd.Timestamp(date(2020,3,12))), 'column_name'] =  'Tag 3'
df.loc[(df['Approved Date'] >= pd.Timestamp(date(2020,3,10))) & (df['Approved Date'] <= pd.Timestamp(date(2020,3,30))), 'column_name'] =  'Tag 4'

df.head(