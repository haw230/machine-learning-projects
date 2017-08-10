# -*- coding: utf-8 -*-
from sklearn import datasets, svm
import matplotlib.pyplot as plt

digits = datasets.load_digits() #dictionary like object

clf = svm.SVC(gamma=0.001, C=100) #classifier is support vector machine

i = -10

X, y = digits.data[:i], digits.target[:i] #set X to data, y to results

clf.fit(X, y) #training

j = -4

plt.imshow(digits.images[j], cmap=plt.cm.gray_r, interpolation='nearest') #displaying
plt.show() #displaying

print(clf.predict(digits.data[j]))
