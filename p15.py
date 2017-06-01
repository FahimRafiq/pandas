import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import style


style.use('fivethirtyeight')

api_key = "Cxe41MDVyJhXQYGuVGx7"

def create_labels(cur_hpi,fut_hpi):
    if fut_hpi > cur_hpi:
        return 1
    else:
        return 0

housing_data = pd.read_pickle('HPI.pickle')
housing_data = housing_data.pct_change()

housing_data.replace([np.inf,-np.inf], np.nan , inplace = True)
housing_data.dropna(inplace=True)

housing_data["US_HPI_future"] = housing_data["US_HPI"].shift(-1)
housing_data['label'] = list(map(create_labels,housing_data["US_HPI"],housing_data["US_HPI_future"]))
print(housing_data.head())


