#!/usr/bin/env python
"""
Suppose you have some texts of news and know their categories.
You want to train a system with this pre-categorized/pre-classified
texts. So, you have better call this data your training set.
"""

from sklearn import tree
import datetime
import csv
import math
import random
import copy

titles = []
data = []
totest = []
result = []
with open('featuresRF.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[0] == "":
            titles = row
        else:
            arow = []
            for entry in row[3:len(row)]:
                if entry == "":
                    arow.append(0)
                elif entry == "TRUE":
                    arow.append(0)
                elif entry == "FALSE":
                    arow.append(1)
                else:
                    arow.append(float(entry))

            if row[2] == "-1":
                totest.append(arow)
            else:
                result.append(float(row[2]))
                data.append(arow)

randomTrees = []

temp = []
for num in range(len(result)):
    temp.append((data[num],result[num]))

for x in range(100):

    random.shuffle(temp)

    # print temp[1]
    clf = tree.DecisionTreeClassifier()

    tempr = []
    tempd = []
    for num in range(1000):
        tempd.append(temp[num][0])
        tempr.append(temp[num][1])
    clf.fit(tempd, tempr)
    randomTrees.append(clf)

    print x

results = []

print "build tree"

for tree in randomTrees:
    results.append(tree.predict_proba(totest))

out = []
for num in range(len(results[0])):
    res = 0
    for rs in results:
        res = res + rs[num][1]
    print res
    re = float(res) / 200.0
    print re
    out.append(re)

csvfile = []
with open('sampleSubmission.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        csvfile.append(row)

for num in range(1, len(csvfile)):
    csvfile[num][1] = out[num-1]

with open('res.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(csvfile)


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
