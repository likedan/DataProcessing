import operator
import copy
from matplotlib import pyplot as plt
import time

def parseTextT(text):
    output = []
    text_file = open(text + ".txt", "r")
    for line in text_file:
        arr = line.split(',')
        if len(arr) == 3:
            arr[2] = arr[2].replace('\n', '')
            arr[2] = int(arr[2])
            output.append((arr[0],arr[1],arr[2]))
    return output

trutharr = parseTextT("truth_normalized")
step1arr = parseTextT("step1")

step1arr = list(set(step1arr))
trutharr = list(set(trutharr))
data_n = []
data_r = []

def findClassOfPoint(data, point):
    for x in xrange(len(data)):
        if point in data[x]:
            return x
            # if point[0] == p[0] and point[1] == p[1]:
            #     return x


for n in xrange(5):
    data_r.append([])

for n in xrange(5):
    data_n.append([])

points = []

for obj in step1arr:
    points.append((obj[0], obj[1]))
    data_n[obj[2]].append((obj[0],obj[1]))

points = list(set(points))

for obj in trutharr:
    data_r[obj[2]].append((obj[0],obj[1]))

for n in data_r:
    n = list(set(n))

for n in data_n:
    n = list(set(n))

intersectionMatrix = []
for x in range(5):
    intersectionMatrix.append([])
    for y in range(5):
        intersectionMatrix[x].append(len(list(set(data_r[x]) & set(data_n[y]))))
for d in data_r:
    print len(d)
print intersectionMatrix

precision = 0.0
recall = 0.0
for p in points:
    realClass = findClassOfPoint(data_r, p)
    normalClass = findClassOfPoint(data_n, p)
    # print realClass
    # print normalClass
    if realClass == 0 and normalClass == 0:
        recall = recall + 1
        precision = precision + 1
    elif realClass == 0:
        recall = recall + 1
        precision = precision + 1 / float(len(data_n[normalClass]))
    elif normalClass == 0:
        recall = recall + 1 / float(len(data_r[realClass]))
        precision = precision + 1
    else:
        precision = precision + float(intersectionMatrix[realClass][normalClass]) / float(len(data_n[normalClass]))
        recall = recall + float(intersectionMatrix[realClass][normalClass]) / float(len(data_r[realClass]))
        # print float(intersectionMatrix[realClass][normalClass]) / float(len(data_r[realClass]))

print precision / len(points)
print recall / len(points)
# for obj in arr:
#     Xs[obj[3]].append(obj[0])
#     Ys[obj[3]].append(obj[1])
#
# Xs = []
# Ys = []
# for n in xrange(5):
#     Xs.append([])
#     Ys.append([])
#
# for line in arr:
#     print line[2]
#     Xs[line[2]].append(line[0])
#     Ys[line[2]].append(line[1])
#
# plt.scatter(Xs[0],Ys[0],color='black')
# plt.scatter(Xs[1],Ys[1],color='blue')
# plt.scatter(Xs[2],Ys[2],color='green')
# plt.scatter(Xs[3],Ys[3],color='red')
# plt.scatter(Xs[4],Ys[4],color='orange')
# plt.show()
