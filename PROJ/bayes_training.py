#!/usr/bin/env python
"""
Suppose you have some texts of news and know their categories.
You want to train a system with this pre-categorized/pre-classified
texts. So, you have better call this data your training set.
"""

import csv
import pymongo
import datetime
from pymongo import MongoClient


client = MongoClient('127.0.0.1', 27017)
db = client['trainDATA']
# db["positive"].remove()

table = db["totest"]

library = {}

with open('test.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == "bidder_id":
            print "first"
        else:
            bidderID = row[0]
            library[row[0]] = {row[2]:1, row[1]:1}

with open('bids.csv', 'rb') as f:
    reader = csv.reader(f)
    count = 0
    for row in reader:
        count += 1
        if row[0] == "bid_id":
            print "first"
        else:
            if library.has_key(row[1]):
                for number in range(2, 9):
                    string = row[number].replace('.', '-')
                    if library[row[1]].has_key(string):
                        library[row[1]][string] = library[row[1]][string] + 1
                    else:
                        library[row[1]][string] = 1
        if count % 5000 == 0:
            print count

for key in library.keys():
    table.insert_one({"_id":key, "info": library[key]})

print "done"
# with open('test.csv', 'rb') as f:
#     reader = csv.reader(f)
#     for row in reader:
#         if row[0] == "bidder_id":
#             print "first"
#         else:
#             testTable.update({"_id": row[0]}, {"_id": row[0], "data": row[1]+" "+row[2]}, upsert = True)

# with open('bids.csv', 'rb') as f:
#     reader = csv.reader(f)
#     count = 0
#     for row in reader:
#         count += 1
#         if row[0] == "bid_id":
#             print "first"
#         else:
#             if not testTable.find_one({"_id": row[1]}) == None:
#                 info = testTable.find_one({"_id": row[1]})
#                 if not len(info["data"]) > 1000:
#                     info["data"] = info["data"] + " " + row[2] + " " + row[3] + " " + row[4] + " " + row[5] + " " + row[6] + " " + row[7] + " " + row[8]
#                     testTable.update({"_id": row[1]}, info, upsert = True)
#


# print "DONE!!!"
# You need to train the system passing each text one by one to the trainer module.
# newsSet =[
#     {'text': 'not to eat too much is not enough to lose weight', "re":"lalala", 'category': 'health'},
#     {'text': 'Russia is trying to invade Ukraine', "re":"hahaha", 'category': 'politics'},
#     {'text': 'do not neglect exercise', "re":"lalala", 'category': 'health'},
#     {'text': 'Syria is the main issue, Obama says', "re":"hahaha", 'category': 'politics'},
#     {'text': 'eat to lose weight', "re":"lalala", 'category': 'health'},
#     {'text': 'you should not eat much', "re":"hahaha", 'category': 'health'}
# ]
#
# for news in newsSet:
#     newsTrainer.train(news['text'], news['category'])
# newsClassifier = Classifier(newsTrainer.data, tokenizer)
#
# unknownInstance = "Even if I eat too much, is not it possible to lose some weight"
# classification = newsClassifier.classify(unknownInstance)
# print classification
