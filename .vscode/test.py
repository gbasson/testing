# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load in 

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib as mpl
import matplotlib.pyplot as plt
x = 'hello'
print(x)

# Load dataset
df = pd.
df = pd.read_csv("C:/Users/GaryBasson/OneDrive - DataMoment/Development/notebooks/kaggle/ny-daily-inmates-in-custody/dataset/daily-inmates-in-custody.csv")
# Describe Data Types
df.dtypes
print(df.dtypes)
#print(df.head(10250))

#print(df.isnull().sum())

#print(df.groupby(['INMATEID', 'INMATEID']).count())
inmate = df.INMATEID.unique()
#print(inmate.groupby(['INMATEID', 'INMATEID']).count())

#print(df.groupby('INMATEID').size())

#print(df['INMATEID'].value_counts())
#print(df['RACE'].value_counts().index.tolist())

df.plot.bar()
%matplotlib inline