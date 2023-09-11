#!/usr/bin/env python3

import pandas as pd
data=pd.read_csv('/home/narmis/Documents/owid-co2-data.csv')
data_clean = data[(data['co2'] > 0) & (data['country'] != 'World')]

print(data)