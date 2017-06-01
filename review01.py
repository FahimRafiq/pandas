import pandas as pd

df = pd.read_csv('ZILL-Z77006_MLP.csv')
df.set_index('Date',inplace=True)
df.rename({'Date':'index'},inplace=True)
print(df.head())