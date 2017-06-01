import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style
style.use('ggplot')


web_stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[34,54,53,64,65,43],
             'Bounce_Rate':[65,72,63,23,43,54]}

df = pd.DataFrame(web_stats)

##print(df)
##print(df.head())
##print(df.tail(2))

##df.set_index('Day',inplace = True)
##
##print(df[['Visitors','Bounce_Rate']])
print(np.array(df.Visitors))
