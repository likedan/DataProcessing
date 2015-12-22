import operator
import copy
import math
from matplotlib import pyplot as plt
import time

def parseText(text):
    output = []
    text_file = open(text + ".txt", "r")
    for line in text_file:
        arr = line.split(',')
        if len(arr) == 2:
            arr[1] = arr[1].replace('\n', '')
            arr[0] = float(arr[0])
            arr[1] = float(arr[1])
            arr.append(False)
            arr.append(-1)
            output.append(arr)
    return output

def findAUnvisited(output):
    for r in output:
        if not r[2]:
            return r
    return None

def getNeighbourArr(node, output, dist):
    neighbours = []
    for n in output:
        if not n == node:
            first = n[0] - node[0]
            second = n[1] - node[1]
            eud = math.sqrt(first * first + second * second)
            if eud < dist:
                neighbours.append(n)
    return neighbours

def getNeighbourArrNum(node, output, dist, num):
    neighbours = []
    for n in output:
        if not n == node:
            first = n[0] - node[0]
            second = n[1] - node[1]
            eud = math.sqrt(first * first + second * second)
            if eud < dist:
                neighbours.append(n)
        if len(neighbours) > num:
            return True
    return False

start = time.clock()
arr = parseText("data_normalized")
node = findAUnvisited(arr)
distance = 0.06
minSupp = 25
existingCluster = 0
while not node == None:
    node[2] = True
    N = getNeighbourArr(node, arr, distance)
    if len(N) > minSupp:
        existingCluster = existingCluster + 1
        node[3] = existingCluster
        for obj in N:
            if not obj[2]:
                obj[2] = True
                NN = getNeighbourArr(obj, arr, distance)
                if len(NN) > minSupp:
                    for p in NN:
                        N.append(p)
            if obj[3] == -1:
                obj[3] = node[3]
    else:
        node[3] = 0
    node = findAUnvisited(arr)

outarr = []
text_file = open("data_normalized.txt", "r")
for line in text_file:
    ar = line.split(',')
    if len(ar) == 2:
        st = line.replace('\n', '')
        outarr.append(st)

print len(outarr)
# print arr
target = open("step2b.txt", 'w')
target.write(str(25))
target.write("\n")
target.write(str(distance))
target.write("\n")
target.write(str(existingCluster))
target.write("\n")

count = 0
for index in xrange(len(arr)):
    count = count + 1
    out = outarr[index]+","+str(arr[index][3]) + "\n"
    target.write(out)
print(count)
elapsed = time.clock()
elapsed = elapsed - start
print elapsed

Xs = []
Ys = []
for n in xrange(existingCluster + 1):
    Xs.append([])
    Ys.append([])

for obj in arr:
    Xs[obj[3]].append(obj[0])
    Ys[obj[3]].append(obj[1])

print len(Xs[0])

plt.scatter(Xs[0],Ys[0],color='black')
plt.scatter(Xs[1],Ys[1],color='blue')
plt.scatter(Xs[2],Ys[2],color='green')
plt.scatter(Xs[3],Ys[3],color='red')
# plt.scatter(Xs[4],Ys[4],color='orange')
plt.show()
