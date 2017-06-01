import pandas as pd
##
##df = pd.read_csv('ZILL-Z77006_MLP.csv')
##df.set_index('Date',inplace = True)
##df.to_csv('newcsv2.csv')
##
##df = pd.read_csv('ZILL-Z77006_MLP.csv',index_col = 0)
##df.columns = ['Austin_HPI']
####print(df.head())
##
##df.to_csv('newcsv3.csv',header = False)

df = pd.read_csv('newcsv3.csv',names=['Date','Austin_HPI'],index_col=0)
df.rename(columns = {'Austin_HPI':'a'},inplace = True)

print(df.head())



