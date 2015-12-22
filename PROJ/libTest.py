#!/usr/bin/env python
"""
Suppose you have some texts of news and know their categories.
You want to train a system with this pre-categorized/pre-classified
texts. So, you have better call this data your training set.
"""
from naiveBayesClassifier import tokenizer
from naiveBayesClassifier.trainer import Trainer
from naiveBayesClassifier.classifier import Classifier
import csv

import pymongo
import datetime
from pymongo import MongoClient

try:
    client = MongoClient('127.0.0.1', 27017)
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e
db = client['testing']
db['trainTable'].remove()
db['testTable'].remove()

from sklearn.ensemble import RandomForestClassifier
X = [[0, 0], [1, 1]]
Y = [0, 1]
clf = RandomForestClassifier(n_estimators=10)
clf = clf.fit(X, Y)
print clf
# trainTable = db['trainTable']
# testTable = db['testTable']
#
# trainT = {}
# testT = {}
# with open('train.csv', 'rb') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         if row[0] == "bidder_id":
#             print "first"
#         else:
#             trainT[str(row[0])] = trainTable.find_one({"_id": row[0]})
#
# with open('test.csv', 'rb') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         if row[0] == "bidder_id":
#             print "first"
#         else:
#             testT[str(row[0])] = testTable.find_one({"_id": row[0]})
#
# newsTrainer = Trainer(tokenizer)
#
# print "DONE!!!"
#
# for txt in trainT.keys():
#     # print trainT[txt]["data"]
#     newsTrainer.train(trainT[txt]["data"], trainT[txt]["result"])
#
# newsClassifier = Classifier(newsTrainer.data, tokenizer)
#
# for txt in testT.keys():
#     # print testT[txt]["data"]
#     classification = newsClassifier.classify(testT[txt]["data"])
#     print classification
#     resul = 0
#     if classification[0][1] + classification[1][1] == 0:
#         resul = 0.5
#     else:
#         if classification[0][0] == "1.0":
#             resul = 1
#         elif classification[0][0] == "0.0":
#             resul = 0
#
#     text_file = open("example.txt", "a")
#     txt = str(resul) + "\n"
#     text_file.write(txt)
#     text_file.close()
#
#
#     # print len(testT[txt]["data"])
# #
# # unknownInstance = "Even if I eat too much, is not it possible to lose some weight"
