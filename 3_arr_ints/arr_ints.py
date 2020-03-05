import random

# a function that returns a random array
def getRandomArray(n):
    distinct = set()
    returnList = []
    while len(distinct) != n:
        randomNumber = random.randrange(1, n+1)
        if randomNumber not in distinct:
            distinct.add(randomNumber)
            returnList.append(randomNumber)
    return returnList


def getSortedArray(n):
    returnList = []
    for i in range(n, 0, -1):
        returnList.append(i)
    return returnList

# print('Random array:', *getRandomArray(10))
# print('Sorted array:', *getSortedArray(10))