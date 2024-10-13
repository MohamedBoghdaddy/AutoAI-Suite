import pandas as pd

df = pd.read_csv('data.csv')
df['new_column'] = df['existing_column'] * 2
df.to_excel('output.xlsx', index=False)
