#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop("TOTAL", 0)
data = featureFormat(data_dict, features)




for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
#for key, value in data_dict.items():
    #if value['bonus']==data.max():

        #print key
        #or
#biggest=0
#for key, value in data_dict.items():
    #if value['bonus']>biggest:
        #biggest=value['bonus']
        #print key
        ### your code below
for user in data_dict:
     if (data_dict[user]['bonus']>5000000 and data_dict[user]['salary']>1000000):
         print user
