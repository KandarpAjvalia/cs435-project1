import random

def getRandomArray(n):
    distinct = set()
    returnList = []
    while(len(distinct) != n):
        randomNumber = random.randrange(0, n)
        if randomNumber not in distinct:
            distinct.add(randomNumber)
            returnList.append(randomNumber)
    return returnList

def getSortedArray(n):
    returnList = []
    for i in range(n - 1, -1, -1):
        returnList.append(i)
    return returnList

print(*getRandomArray(10))
print(*getSortedArray(10))