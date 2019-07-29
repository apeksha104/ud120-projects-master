#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

#print(len(enron_data))
#print(len(enron_data.keys()))
#print(len(enron_data.values()[0]))
#count=0
#for user in enron_data:
    #if enron_data[user]['poi']==True:
        #count=count+1
#print count
#print(enron_data['PRENTICE JAMES']['total_stock_value'])
#print(enron_data['COLWELL WESLEY']['from_this_person_to_poi'])
#print(enron_data['SKILLING JEFFREY K']['exercised_stock_options'])
#print(enron_data['SKILLING JEFFREY K']['total_payments'])
#print(enron_data['FASTOW ANDREW S']['total_payments'])
#print(enron_data['LAY KENNETH L']['total_payments'])
#print(enron_data)
count_sal=0
count_mail=0
for key in enron_data.keys():
    if enron_data[key]['salary']!='NaN':
        count_sal=count_sal+1
    if enron_data[key]['email_address']!='NaN':
        count_mail+=1
print(count_sal)
print(count_mail)
