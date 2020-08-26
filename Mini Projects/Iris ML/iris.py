# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 12:19:30 2020

@author: Anobhama
"""

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier


#loading the data sets
iris=datasets.load_iris()
features=iris.data
labels=iris.target
#print(features[0],labels[0])

#tesing 
clf=KNeighborsClassifier()
clf.fit(features,labels)


preds=clf.predict([[4.6,3.4,1.4,0.3]])
print(preds)


preds=clf.predict([[5.2,2.7,3.9,1.4]])
print(preds)


preds=clf.predict([[6.2,2.8,4.8,1.8]])
print(preds)

"""
[0] -> Iris-setosa
[1] -> Iris-versicolor
[2] -> Iris-virginica
"""
