#!/usr/bin/env python
from scipy import stats
import numpy as np
import csv
import matplotlib.pyplot as plt
traindata = []
testdata = []
titles = []
with open('features.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        if row[2] == "0.0" or row[2] == "1.0":
            traindata.append(row)
        elif row[2] == "-1.0":
            testdata.append(row)
        else:
            titles = row

train_outcome = []
testingx = []
testingy = []
for data in traindata:
    if data[titles.index("n_urls")] == "" or data[titles.index("bids_per_auction_mean")] == "":
        print "empty"
    else:
        train_outcome.append(float(data[2]))
        testingx.append(float(data[titles.index("n_urls")]))
        testingy.append(float(data[titles.index("bids_per_auction_mean")]))

# bigarr = [[] for x in range(72)]
# for d
x = np.array(testingx)
y = np.array(testingy)
z = np.array(train_outcome)
plt.scatter(x, y, c=z)
# plt.xlim(-1,2)
plt.show()

print "DONE!!!"
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
