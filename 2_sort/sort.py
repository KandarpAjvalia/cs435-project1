import random

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


outputList = []

# insert a node in the bst recursively
def insertRec(currentNode, nodeToInsert):
    if currentNode is None:
        return nodeToInsert
    if nodeToInsert.data < currentNode.data:
        currentNode.left = insertRec(currentNode.left, nodeToInsert)
    else:
        currentNode.right = insertRec(currentNode.right, nodeToInsert)
    return currentNode


# in-order traversal, instead of printing, we append to the output list
def inOrder(root):
    if root:
        global outputList
        inOrder(root.left)
        outputList.append(root.data)
        inOrder(root.right)

# creates a bst from a given list and returns a sorted list
def sort(unsortedList):
    root = insertRec(None, Node(unsortedList[0]))

    for n in unsortedList[1:]:
        insertRec(root, Node(n))

    inOrder(root)

    return outputList


unsortedList = [3, 6, 1, 9, 11, 2, 5, 4]

sort(unsortedList)

print(*outputList)