import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import tree
import graphviz
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import plot_tree
from sklearn.metrics import confusion_matrix

df = pd.read_csv('test.csv')

df=pd.get_dummies(data=df, drop_first=True)
#remove nan
df=df.dropna()
#split data}
print(df.head())
X = df.drop('satisfaction_satisfied', axis=1)
y = df['satisfaction_satisfied']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
clf = DecisionTreeClassifier(max_depth=5)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(clf.score(X_test, y_test))
plt.figure(figsize=(20,20))
plot_tree(clf, filled=True, rounded=True, class_names=['Unsatisfied', 'Satisfied'], feature_names=X.columns, fontsize=8)
plt.show()
#random forest
rf = RandomForestClassifier(n_estimators=100, max_depth=5)
rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)
print(confusion_matrix(y_test, y_pred))
print(rf.score(X_test, y_test))


