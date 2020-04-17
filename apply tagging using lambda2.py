#add tagging to items based on 1st number

#get first number and store it to a variable
first_number = df['Document Number'].str[:1].astype(int)

#tagging using lambda
df['PR_Doctype'] = first_number.apply(lambda x: 'Series-1' if x == 1 else 'Series-5' if x == 5 else 'Series-4' if x == 4 else 'Series-6' if x == 6 else 'Series-7' if x == 7 else '')
df.head()
