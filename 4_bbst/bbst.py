import sys
import time


sys.path.append('../3_arr_ints')
sys.path.append('../1_bst')

# print(sys.path)

import arr_ints
import bst

# creating a structure of node
class Node:
    def __init__(self, data):
        self.data = data
        self.height = 1
        self.left = None
        self.right = None

    def __str__(self):
        return 'node data: {}'.format(self.data)

# Initializing node as null
root = None
travCount = 0


def incrementTrav():
    global travCount
    travCount += 1


def calcHeight(node):

    leftHeight = 0
    rightHeight = 0

    if node and node.left:
        leftHeight = node.left.height
    if node and node.right:
        rightHeight = node.right.height

    return max(leftHeight, rightHeight) + 1


def balanceFactor(node):
    leftHeight = 0
    rightHeight = 0

    if node and node.left:
        leftHeight = node.left.height
    if node and node.right:
        rightHeight = node.right.height

    return leftHeight - rightHeight


def isBalanced(node):
    if node:
        return -1 <= balanceFactor(node) <= 1
    return 1


def leftRotate(node):

    temp = node.right
    node.right = temp.left
    temp.left = node

    node.height = calcHeight(node)
    temp.height = calcHeight(temp)

    return temp

def rightRotate(node):

    temp = node.left
    node.left = temp.right
    temp.right = node

    node.height = calcHeight(node)
    temp.height = calcHeight(temp)

    return temp


def balance(node):

    bf = balanceFactor(node)

    if bf > 1:
        leftBal = balanceFactor(node.left)
        if leftBal < 0:
            node.left = leftRotate(node.left)

        node = rightRotate(node)
        return node
    else:
        rightBal = balanceFactor(node.right)
        if rightBal > 0:
            node.right = rightRotate(node.right)
        node = leftRotate(node)
    return node


# a function to insert a node in a bst iteratively
def insertIter(rootGiven, nodeToInsert):
    # if node is none, return pointer to the given node
    if rootGiven is None:
        return nodeToInsert

    # pointers to keep track of our position in the tree
    curr = rootGiven
    parent = None
    insertData = nodeToInsert.data
    stackSim = []
    path = []

    # slide down left or right depending on the conditions
    while curr is not None:
        currData = curr.data
        parent = curr
        # add parents of our traversal to the stack
        stackSim.append(parent)

        if insertData < currData:
            curr = curr.left
            path.append('L')
        else:
            path.append('R')
            curr = curr.right
        incrementTrav()

    # insert on left if element is smaller than parent,
    # else insert to the right
    if insertData < parent.data:
        parent.left = nodeToInsert
    else:
        parent.right = nodeToInsert

    isFirst = True
    path.pop()
    prev = None

    # check balance factor for each parent
    for node in stackSim[::-1]:
        if not isFirst:
            if path.pop() is 'R':
                node.right = prev
            else:
                node.left = prev
        if not isBalanced(node):
            node = balance(node)
        prev = node
        isFirst = False
        node.height = calcHeight(node)
    global root
    root = prev
    # return pointer to the inserted element's parent
    return parent


def deleteIterHelper(currentNode):
    global root
    parent = root
    tempNode = root.left

    # this part may be reduced by using findNext function
    # find next biggest element's parent node
    while tempNode.right:
        # print('inside while')
        parent = tempNode
        tempNode = tempNode.right

    currentNode.data = tempNode.data

    # print('parent node: ', parent.data)
    #
    # print('temp node: ', tempNode.data)

    # if next biggest's left is empty but has right children, move child left or right
    if tempNode.left:
        if tempNode.left.data < parent.data:
            parent.left = tempNode.left
        elif tempNode.left.data > parent.data:
            parent.right = tempNode.left

    # if there's no right node
    else:
        if tempNode.data < parent.data:
            parent.left = None
        else:
            parent.right = None


# a function to delete a node from bst recursively
def deleteIter(currentNode, nodeToDelete):

    parent = None
    global root

    # check if given node(node) is empty
    if currentNode is None:
        return

    # if node is to be deleted
    elif currentNode.data == nodeToDelete.data:
        # check left and right nodes if they are empty,
        # return None(null pointer) because tree is empty
        if currentNode.left is None and currentNode.right is None:
            root = None

        # if there is a left child and no right child, node becomes left child
        elif currentNode.left and currentNode.right is None:
            root = currentNode.left

        # if there is a right child and no left child, node becomes right child
        elif currentNode.left is None and currentNode.right:
            root = currentNode.right

        # if there are two children of node, we make node the next bigger element of node as node
        elif currentNode.left and currentNode.right:
            deleteIterHelper(currentNode)
            if not isBalanced(currentNode):
                root = balance(currentNode)
                return root
        if not isBalanced(currentNode):
            root = balance(currentNode)
            root.height = calcHeight(root)
        return root


    temp = currentNode
    deletionData = nodeToDelete.data

    stackSim = []
    path = []


    # if node is not a node, we just slide down to the node we want to delete
    while temp and temp.data != deletionData:
        parent = temp

        stackSim.append(parent)

        if deletionData < temp.data:
            temp = temp.left
            path.append('L')

        elif deletionData > temp.data:
            temp = temp.right
            path.append('R')

    # if we don't find the node in
    if temp is None:
        return

    # check left and right nodes if they are empty,
    # set parent's left or right as None depending on condition
    if temp.left is None and temp.right is None:
        if deletionData < parent.data:
            parent.left = None
        else:
            parent.right = None

    # if left node exists but no right node
    elif temp.left and temp.right is None:
        if deletionData < parent.data:
            parent.left = temp.left
        else:
            parent.right = temp.left

    # if left node exists but no right node
    elif temp.left is None and temp.right:
        if deletionData < parent.data:
            parent.left = temp.right
        else:
            parent.right = temp.right

    # if two children of current node exist
    else:
        deleteIterHelper(temp)
        if not isBalanced(currentNode):
            root = balance(currentNode)
            root.height = calcHeight(root)
            return

    isFirst = True
    path.pop()

    prev = None
    # print(*stackSim)
    # print(path)
    # check balance factor for each parent
    for node in stackSim[::-1]:
        if not isFirst:
            if path.pop() is 'R':
                node.right = prev
            else:
                node.left = prev
        # print('bf of {} is {}'.format(node, balanceFactor(node)))
        if not isBalanced(node):
            node = balance(node)
        prev = node
        isFirst = False
        node.height = calcHeight(node)
    # print('prev data', prev.data)
    root = prev


# an iterative function to find the next node greater than a given node
def findNextIter(currentNode, data):
    temp = currentNode

    # slide down to the node we want to find next of
    while temp and temp.data != data:
        if data < temp.data:
            temp = temp.left
        elif data > temp.data:
            temp = temp.right

    # follow path node->right then node->right->leftmost
    slider = None
    if temp.right:
        slider = temp.right
        while slider.left:
            slider = slider.left
        return slider

    # if right node does not exist
    while currentNode:
        if temp.data < currentNode.data:
            slider = currentNode
            currentNode = currentNode.left
        elif temp.data > currentNode.data:
            currentNode = currentNode.right
        else:
            break

    return slider


# an iterative function to find the previous node smaller than a given node
def findPrevIter(currentNode, data):
    if currentNode is None:
        return currentNode

    prevNode = None
    temp = currentNode

    # slide down to the node we want to find prev of
    while temp and temp.data != data:
        if data < temp.data:
            temp = temp.left
        elif data > temp.data:
            prevNode = temp
            temp = temp.right

    # follow path node->left then node->left->rightmost
    if temp and temp.left:
        slider = temp.left
        while slider.right:
            slider = slider.right
        return slider
    return prevNode


# an iterative function to find the min of bst
def findMinIter(currentNode):

    # if given node is none
    if currentNode is None:
        return currentNode

    # go all the way to the left of the tree and return that node's data
    temp = currentNode
    while temp.left:
        temp = temp.left
    return temp.data


# an iterative function to find the min of bst
def findMaxIter(currentNode):

    # if given node is none
    if currentNode is None:
        return currentNode

    # go all the way to the right of the tree and return that node's data
    temp = currentNode
    while temp.right:
        temp = temp.right
    return temp.data


# print bst in order
def printBbst(root):
    if root:
        printBbst(root.left)
        print(root.data, end=' ')
        printBbst(root.right)


# Part 5a
print('Part 5.a. --- Random Array')
randomArray = arr_ints.getRandomArray(10000)

bst.root = bst.insertRec(None, bst.Node(randomArray[0]))

for n in randomArray[1:]:
    bst.insertRec(bst.root, bst.Node(n))

print('created bst from 10000 elements -- Recursive')

root = insertIter(None, Node(randomArray[0]))
for n in randomArray[1:]:
    insertIter(root, Node(n))

print('created avl tree from 10000 elements -- Iterative')

# Part 5c
print('\n\nPart 5.c. --- Random Array')
randomArray = arr_ints.getRandomArray(10000)

bst.root = bst.insertIter(None, bst.Node(randomArray[0]))

for n in randomArray[1:]:
    bst.insertIter(bst.root, bst.Node(n))

print('created bst from 10000 elements -- Iterative')


root = insertIter(None, Node(randomArray[0]))
for n in randomArray[1:]:
    insertIter(root, Node(n))
print('created avl tree from 10000 elements -- Iterative')


# Part 6b
print('\n\nPart 6.b. --- Random Array')
randomArray = arr_ints.getRandomArray(10000)

bst.root = bst.insertIter(None, bst.Node(randomArray[0]))

for n in randomArray[1:]:
    bst.insertIter(bst.root, bst.Node(n))

print('bst child traversal: ', bst.travCount)

root = insertIter(None, Node(randomArray[0]))
for n in randomArray[1:]:
    insertIter(root, Node(n))

print('avl child traversal: ', travCount)


# Part 6c
print('\n\nPart 6.c. --- Sorted Array')
sortedArray = arr_ints.getSortedArray(10000)

bst.root = bst.insertIter(None, bst.Node(sortedArray[0]))

for n in sortedArray[1:]:
    bst.insertIter(bst.root, bst.Node(n))

print('bst child traversal: ', bst.travCount)

root = insertIter(None, Node(sortedArray[0]))
for n in sortedArray[1:]:
    insertIter(root, Node(n))

print('avl child traversal: ', travCount)



# Extra Credit
# 7.a.
# Use the code from ../extracredit_credit(7).py
