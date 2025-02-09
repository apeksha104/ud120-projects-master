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
from sklearn.svm import SVC
import numpy as np
from sklearn.metrics import accuracy_score
clf=SVC(kernel='rbf', C=10000.0)
t0=time()

clf.fit(features_train, labels_train)
print "training time:", round(time()-t0, 3), "s"
t0=time()
pred=clf.predict(features_test)
count=0
i=0
for n in pred:

    if pred[i]==1:
        count=count+1
    i=i+1

print(count)
print "predicting time:", round(time()-t0, 3), "s"
print(accuracy_score(labels_test, pred))### your code goes here ###

#########################################################
