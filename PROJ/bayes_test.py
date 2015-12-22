#!/usr/bin/env python
"""
Suppose you have some texts of news and know their categories.
You want to train a system with this pre-categorized/pre-classified
texts. So, you have better call this data your training set.
"""

import pymongo
import datetime
from pymongo import MongoClient
import csv
import math

try:
    client = MongoClient('127.0.0.1', 27017)
    print "Connected successfully!!!"
except pymongo.errors.ConnectionFailure, e:
   print "Could not connect to MongoDB: %s" % e
db = client['trainDATA']
positive = db["positive"]
negative = db["negative"]
totest = db["totest"]

negativeData = {}
positiveData = {}

ng = negative.find()
for n in ng:
    for key in n["info"].keys():
        if negativeData.has_key(key):
            negativeData[key] = negativeData[key] + n["info"][key]
        else:
            negativeData[key] = n["info"][key]

ps = positive.find()
for p in ps:
    for key in p["info"].keys():
        if positiveData.has_key(key):
            positiveData[key] = positiveData[key] + p["info"][key]
        else:
            positiveData[key] = p["info"][key]

k = 10

def getNegativeP(string):
    if not positiveData.has_key(string):
        positiveData[string] = 0
    if not negativeData.has_key(string):
        negativeData[string] = 0
    return (float(negativeData[string]) + k) / (float(positiveData[string]) + float(negativeData[string]) + k)

def getPositiveP(string):
    if not positiveData.has_key(string):
        positiveData[string] = 0
    if not negativeData.has_key(string):
        negativeData[string] = 0
    return (float(positiveData[string]) + k) / (float(positiveData[string]) + float(negativeData[string]) + k)

csvfile = []
with open('sampleSubmission.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        csvfile.append(row)

for row in csvfile:
    if not row[0] == "bidder_id":
        negativeRate = math.log(float(negative.count()) / float(negative.count() + positive.count()))
        positiveRate = math.log(float(positive.count()) / float(negative.count() + positive.count()))
        entry = totest.find_one({"_id":row[0]})
        for word in entry["info"].keys():
            negativeRate = negativeRate + math.log(getNegativeP(word))
            positiveRate = positiveRate + math.log(getPositiveP(word))

        print str(negativeRate) + "  " + str(positiveRate)

        if float(positiveRate) / float(negativeRate) > 0.5:
            row[1] = 1
        else:
            row[1] = 0
with open('hahaha.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(csvfile)

            # bidderID = row[0]
            # library[row[0]] = {row[2]:1, row[1]:1}


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
