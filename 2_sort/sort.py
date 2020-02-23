import random

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insertRec(currentNode, nodeToInsert):
    if currentNode is None:
        return nodeToInsert
    if nodeToInsert.data < currentNode.data:
        currentNode.left = insertRec(currentNode.left, nodeToInsert)
    else:
        currentNode.right = insertRec(currentNode.right, nodeToInsert)
    return currentNode


def inOrder(root):
    if root:
        global outputList
        inOrder(root.left)
        outputList.append(root.data)
        inOrder(root.right)


unsortedList = [3, 6, 1, 9, 11, 2, 5, 4]
root = insertRec(None, Node(unsortedList[0]))

for i in range(1, len(unsortedList)):
    insertRec(root, Node(unsortedList[i]))

outputList = []

inOrder(root)
print(*outputList)