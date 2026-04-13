# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 10:39:04 2026

@author: GoranAndrejevic
"""
import numpy as np
import pandas as pd
import seaborn as sns

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
df = pd.read_csv("https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv")
df
# Zylnders vorhersage: Zylinder abhängige Variable , mpg und hp unahängige Variable

y = df["cyl"] #unabhängige Variable
X = df[["mpg", "hp"]] #abhängige variable
y
X

#Teile in Train und Test Datensätze

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.66, random_state=0)

clf = RandomForestClassifier() #Instance von der Klasse erstellen
clf.fit(X_train, y_train)  #RandomForestClassifier versucht Zusammenhang zwischen unabhängien Variable und abhängigen Variable zu finden
y_predict = clf.predict(X_test)  #RandomForestClassifier versucht die Vorhersage für test Daten zu treffen, y_predict ist ein Array

y_test

y_predict

#Genaugkeit bestimmen

from sklearn.metrics import confusion_matrix

output = confusion_matrix(y_test, y_predict)
output

accuracy = confusion_matrix(y_test, y_predict).diagonal().sum() / confusion_matrix(y_test, y_predict).sum()
print(f"Accuracy is: {accuracy*100}")

feature_importance = pd.Series(clf.feature_importances_, index=X.columns)
feature_importance  # Welche unabghängige Variable ist bessere predictor
feature_importance.plot(kind="bar")
