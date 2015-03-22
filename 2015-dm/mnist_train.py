#! /usr/bin/python
# -*- coding: utf-8 -*-

from matplotlib import pyplot as plt
from sklearn import cross_validation, datasets
from sklearn.linear_model import LogisticRegression

from time import time


print('1. data acquisition')
'''
# Option 1
d = datasets.fetch_mldata('MNIST original', data_home='.')
X = d['data']
y = d['target']
'''

# Option 2
from numpy import genfromtxt
X = genfromtxt('mnist-x-bin.csv', delimiter=',')
y = genfromtxt('mnist-y-bin.csv', delimiter=',')

print('2. data exploration')
print("X[0]:", X[0])
print("y[0]:", y[0])
print("min/max(X[0]):", min(X[0]), max(X[0]))
print("All classes of y:", set(y))

X0 = X[0].reshape(28, 28)           # reshape 1*784 array to 28*28 array
plt.rc('image', cmap='binary')      # set runtime configurations (rc) for color maps
plt.matshow(X0)                     # plot matrix
plt.savefig('X0.png')               # save plot to image file


print('3. data partitioning')
X_train, X_test, y_train, y_test =\
        cross_validation.train_test_split(X, y, test_size=0.4, random_state=1234)

print('4. training')
lr2 = LogisticRegression(random_state=1234)      # LR instance 생성
lr2.fit(X_train, y_train)                        # LR 학습

print('5. testing')
print("Training accuracy:", lr2.score(X_train, y_train))
print("Testing accuracy:", lr2.score(X_test, y_test))

from sklearn.metrics import precision_recall_fscore_support
y_pred = lr2.predict(X_test)
print("PRFS:", precision_recall_fscore_support(y_test, y_pred, average='macro'))
