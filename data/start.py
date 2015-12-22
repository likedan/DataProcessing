import operator
import copy

def parseText(text):
    dict = []
    text_file = open(text + ".txt", "r")
    for line in text_file:
        arr = line.split(' ')
        arr.pop()
        dict.append(frozenset(arr))
    return dict

def doFirst(rawData, frequentPattern):
    diction = {}
    for sets in rawData:
        for idd in sets:
            if diction.has_key(idd):
                diction[idd] = diction[idd] + 1
            else:
                diction[idd] = 1
    keys = diction.keys()
    remaining = {}
    for key in keys:
        if diction[key] > min_support:
            remaining[key] = diction[key]
            frequentPattern[key] = diction[key]
    return remaining

def getCombination(theList, result, num, diction):
    if len(result) < num:
        for index in range(len(theList)):
            temp = list(result)
            temp.append(theList[index])
            copy = list(theList)
            copy.pop(index)
            getCombination(copy, temp, num, diction)
    else:
        theSet = frozenset(result)
        diction[theSet] = 0

def doTheRest(data, num, frequentPattern):
    diction = {}
    getCombination(data.keys(), [], num, diction)
    for sets in rawData:
        for key in diction:
            if sets | key == sets:
                diction[key] = diction[key] + 1
    keys = diction.keys()
    remaining = {}
    for key in keys:
        if diction[key] > min_support:
            remaining[key] = diction[key]
            frequentPattern[key] = diction[key]
    return remaining

def printFile(frequentPattern, fileName, dictionary):
    text_file = open(fileName, "w")
    for item in frequentPattern:
        text = str(item[1]) + " "
        if type(item[0]) is frozenset:
            for elem in item[0]:
                text = text + dictionary[elem] + " "
            text = text[:-1]
        else:
            text = text + dictionary[item[0]]
        text = text + "\n"
        text_file.write(text)
    text_file.close

def mineText(rawData):
    frequentPattern = {}
    data = doFirst(rawData, frequentPattern)
    index = 2
    while len(data) > 0:
        data = doTheRest(data, index, frequentPattern)
        index =+ 1
    return list(reversed(sorted(frequentPattern.items(), key=operator.itemgetter(1))))

def findClosePattern(rawData):
    diction = {}
    print rawData
    for pattern in rawData:
        if diction.has_key(pattern[1]):
            diction[pattern[1]].append(pattern[0])
        else:
            diction[pattern[1]] = [pattern[0]]
    result = []
    for pattern in rawData:
        if len(diction[pattern[1]]) == 1:
            result.append(pattern)
        else:
            isClosePattern = True
            for sameSupport in diction[pattern[1]]:
                if sameSupport != pattern[0]:
                    patt = pattern[0]
                    if type(sameSupport) is str:
                        sameSupport = frozenset([sameSupport])
                    if type(patt) is str:
                        patt = frozenset([patt])
                    if sameSupport | patt == sameSupport:
                        isClosePattern = False
                        print "is not ClosePattern **************************************************************************"
                        print patt
                        print pattern
                        print sameSupport
            if isClosePattern:
                result.append(pattern)

    return result

def findMaxPattern(rawData):
    result = []
    for pattern in rawData:
        isMaxPattern = True
        if type(pattern[0]) is str:

            for check in rawData:
                if type(check[0]) is frozenset:
                    if pattern[0] in check[0]:
                        isMaxPattern = False
                        if pattern[0] == "390":
                            print pattern[0]
                            print check[0]
        else:
            for check in rawData:
                if check[0] != pattern[0]:
                    if type(check[0]) is frozenset:
                        if pattern[0] | check[0] == check[0]:
                            isMaxPattern = False
        if isMaxPattern:
            result.append(pattern)
    return result

min_support = 100
dictionary = {}
text_file = open("vocab.txt", "r")
for line in text_file:
    theline = line[:-1]
    arr = theline.split('\t')
    dictionary[arr[0]] = arr[1]
text_file.close()

for num in xrange(5):
    print str(num) +  "  ***************************************"
    rawData = parseText("topic-"+str(num))
    data = mineText(rawData)
    printFile(data, "pattern-" + str(num)+".txt", dictionary)
    closePattern = findClosePattern(copy.deepcopy(data))
    printFile(closePattern, "close-" + str(num)+".txt", dictionary)
    maxPattern = findMaxPattern(copy.deepcopy(data))
    printFile(maxPattern, "max-" + str(num)+".txt", dictionary)
