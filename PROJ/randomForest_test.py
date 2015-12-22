#!/usr/bin/env python
"""
Suppose you have some texts of news and know their categories.
You want to train a system with this pre-categorized/pre-classified
texts. So, you have better call this data your training set.
"""

from sklearn.ensemble import RandomForestClassifier
import datetime
import csv
import math
import numpy as np

titles = []
result = []
data = []
totest = []
with open('features.csv', 'rb') as f:
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

forest = RandomForestClassifier(n_estimators=10)
forest.fit(data, result, sample_weight=None)

importances = forest.feature_importances_
std = np.std([tree.feature_importances_ for tree in forest.estimators_],
             axis=0)
indices = np.argsort(importances)[::-1]

# Print the feature ranking
print("Feature ranking:")

for f in range(len(indices)):
    print " feature " + titles[3 + indices[f]] + " " + str(importances[indices[f]])

result = forest.predict_proba(totest)

# for r in result:
    # print r
csvfile = []
with open('sampleSubmission.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        csvfile.append(row)

for num in range(1, len(csvfile)):
    csvfile[num][1] = result[num-1][1] / (result[num-1][0] + result[num-1][1])

#
# for row in csvfile:
#     if not row[0] == "bidder_id":
#         negativeRate = math.log(float(negative.count()) / float(negative.count() + positive.count()))
#         positiveRate = math.log(float(positive.count()) / float(negative.count() + positive.count()))
#         entry = totest.find_one({"_id":row[0]})
#         for word in entry["info"].keys():
#             negativeRate = negativeRate + math.log(getNegativeP(word))
#             positiveRate = positiveRate + math.log(getPositiveP(word))
#
#         print str(negativeRate) + "  " + str(positiveRate)
#
#         if float(positiveRate) / float(negativeRate) > 0.5:
#             row[1] = 1
#         else:
#             row[1] = 0
with open('ans.csv', 'wb') as f:
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
