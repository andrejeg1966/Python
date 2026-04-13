# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 11:04:48 2026

@author: GoranAndrejevic
"""

import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

#load full titanic dataset
df_full = pd.read_csv("C:/Dev/KI/Python/\ML Project/titanic_full.csv")
df_full
df_full.set_index("PassengerId", inplace=True)
df_full
df_full.shape

#split full titanic dataset into train and test dataset
df_train = df_full.iloc[:1000,:]
df_test = df_full.iloc[1000:,:]
print("Shape of new dataframes - {} , {}".format(df_train.shape, df_test.shape))

#save the train and test dataset

df_train.to_csv("titanic_train.csv")
df_test.to_csv("titanic_test.csv")


