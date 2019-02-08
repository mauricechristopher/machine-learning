# Exercise 01: DataFrame

# Create a two-dimensional labeled data structure with columns of potentially different types using a DataFrame
# data = {'Country': ['Belgium',  'India',  'Brazil'],
# 'Capital': ['Brussels',  'New Delhi',  'Brasilia'],
# 'Population': [11190846, 1303171035, 207847528]}

import pandas as pd 

data = {'Country': ['Belgium',  'India',  'Brazil'],
'Capital': ['Brussels',  'New Delhi',  'Brasilia'],
'Population': [11190846, 1303171035, 207847528]}

df = pd.DataFrame(data=data)
print(df)