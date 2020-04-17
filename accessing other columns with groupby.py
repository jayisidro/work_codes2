df = df[['column1','column2','column3','column4', 'values5']]

#grouping columns 1-4 and add values in 'values5' column
df2 = df.groupby(['column1','column2','column3','column4'], as_index=False).sum()
df2