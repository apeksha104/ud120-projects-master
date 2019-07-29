#!/usr/bin/python

"""
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np

#dtree=DecisionTreeClassifier(criterion='gini', max_depth=1)
clf=RandomForestClassifier(n_estimators=10)
clf=clf.fit(features_train, labels_train)

pred=clf.predict(features_test)
print(accuracy_score(labels_test,pred))### your code goes here ###

#########################################################
