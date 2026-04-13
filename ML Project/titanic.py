# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 10:11:22 2026

@author: GoranAndrejevic
"""

#import numpy as np
import pandas as pd
import seaborn as sns


#**************************Daten Validierung*************************

train = pd.read_csv("C:/Dev/KI/Python/\ML Project/titanic_train.csv")
test = pd.read_csv("C:/Dev/KI/Python/ML Project/titanic_test.csv")

#Zeige Anzahl von NaN Werte
train.isnull().sum()
#Visualisiere der Anzahl von NaN Werte
sns.heatmap(train.isnull())
#Zeige Anzahl von werten
train["Survived"].value_counts()
train["Survived"].value_counts(normalize=True) * 100
train["Survived"].value_counts().plot(kind="pie")

for col in train.columns:
    try:
        sns.displot(train[col])
    except:
        pass

pd.crosstab(train["Pclass"], train["Survived"], margins=True)
sns.barplot(data=train, x="Pclass", y="Survived")

pd.crosstab(train["Sex"], train["Survived"], margins=True)
sns.barplot(data=train, x="Sex", y="Survived")

sns.barplot(data=train, x="Embarked", y="Survived")
sns.catplot(data=train, y="Embarked", hue="Survived", kind="count")

#sns.violinplot("Age", hue="Survived", data=train)
#sns.violinplot("Sex", "Age", hue="Survived", data=train)

sns.barplot(data=train, x="Sex", y="Survived", hue="Pclass")
#sns.heatmap(train.corr(), annot=True)

PassengersIds = test["PassengerId"]
df = pd.concat([train, test])

#Nicht ausagekräftige Variable rausschmiessen aus dem Model
df.drop(columns=["PassengerId", "Ticket", "Cabin"], inplace=True)

#Variable Name modifizieren
#The Title extrahieren aus dem String: "Mr", "Mrs
"Cumings, Mrs. John Bradley (Florence Briggs Thayer)".split(",")[1].split(".")[0].strip()

df["Title"] = df["Name"].apply(lambda x: x.split(",")[1].split(".")[0].strip())
df.drop("Name", axis=1, inplace=True)
df["Title"].value_counts()

#Nur Mr, Miss, Mrs, Master werden als Title betrachtet, alle andere rausgeschmiessen

#Einige Title strings ersetzen
replacements = [("Mme", "Mrs"), ("Don", "Mr"), ("Dona", "Mrs"), ("Lady", "Mrs"), ("Ms", "Miss")]
replacements

for item in replacements:
    df["Title"] = df["Title"].str.replace(item[0], item[1])

df["Title"] = df["Title"].apply(lambda x: "Other" if x not in ["Mr", "Mrs", "Miss", "Master"] else x)

#Fehlwerte pro Zeile ersetzen. ersetzen sinnvoller dort wo weniger sie sind. Damit das Model represantativ ist
df.isnull().sum()

#Ersetzten Fehlwerte von Age mit Age Median
df["Age"].fillna(df["Age"].median(), inplace=True)
#Ersetzen auch die anderen
df["Fare"].fillna(df["Fare"].median(), inplace=True)

#Embarked ersetzen mit dem häufigsten Wert _> mode
df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

#Entfernen Alle Variable nach dem Embarked, Title bleibt -> Entefernen von Spalten
df.drop(["WikiId", "Name_wiki", "Age_wiki", "Hometown", "Boarded", "Destination", "Lifeboat", "Body", "Class"], axis=1, inplace=True)

#Neue Variable Family einfügen
df["Family"] = df["SibSp"] + df["Parch"] + 1
df.drop(columns=["Parch", "SibSp"], inplace= True)

#Family variable kategorisieren

def family_size(x):
    if x == 1:
        return "Single"
    elif x==2:
        return "Couple"
    else:
        return "Family"
    
df["Family"] = df["Family"].apply(family_size)

#Damy Variable erstellen von den Kategorisierten Variablen

df = pd.get_dummies(df, columns=["Pclass", "Sex", "Embarked", "Title", "Family"], prefix="d", drop_first=True)

#Die grössere standard Abweichung beeinflöusst ML Model mehr
df["Age"].std()
df["Fare"].std()


"""
******************ML mit Scikit. Normalisierung...**********
"""

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler
df[["Age", "Fare"]] = scaler.fit_transform(df[["Age", "Fare"]])

#DataFrame wieder in Test und Train splitten
train = df.iloc[0:len(train), :]
test = df.iloc[len(train):len(df), :]

from sklearn.ensemble import RandomForestClassifier, AdaBoostClassifier, GradientBoostingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

random_state = 0
classfiers = []
classfiers.append(LogisticRegression())
classfiers.append(KNeighborsClassifier())
classfiers.append(DecisionTreeClassifier())
classfiers.append(RandomForestClassifier())
classfiers.append(AdaBoostClassifier(DecisionTreeClassifier()))
classfiers.append(GradientBoostingClassifier())
classfiers
#Spliten Training Datensatz in unabhängige Variablen und abhängige "Survived" Variable
y = train["Survived"]
X = train.drop("Survived", axis=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=random_state)

#from sklearn.model_selection import cross_val_score

#cms = []
#for clf in classfiers:
#   cms.append(cross_val_score(clf, X_train, y_train, cv=10))
#cms
#[x.mean for x in cms]

# Die Schleife hat Errors, aber der GradientBoostingClassifier sollte gewonnen haben mit über 80% treffequete
#Besser veruschen einzel zu testen

parameters = {
    "n_estimators": [5,50,250,500],
    "max_depth": [1,3,5,7,9],
    "learning_rate": [0.01, 0.1,5,10]
}

from sklearn.model_selection import GridSearchCV
clf = GradientBoostingClassifier()
cv = GridSearchCV(clf, parameters, cv=5)
cv.fit(X_train, y_train)
cv.best_params_

test.drop("Survived", inplace=True, axis=1)
y_pred = cv.predict(test)



