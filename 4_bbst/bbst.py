import sys
import time

sys.path.append('../3_arr_ints')

# print(sys.path)

import arr_ints

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
        return abs(balanceFactor(node)) <= 1
    return 1


def leftRotate(node):
    print('left rotate on: ', node.data)
    temp = node.right
    node.right = temp.left
    temp.left = node

    node.height = calcHeight(node)
    temp.height = calcHeight(temp)

    return temp

def rightRotate(node):
    print('right rotate on: ', node.data)

    temp = node.left
    node.left = temp.right
    temp.right = node

    node.height = calcHeight(node)
    temp.height = calcHeight(temp)

    return temp

def balance(node):
    print('balancing')

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

    print('parent node: ', parent.data)

    print('temp node: ', tempNode.data)

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
                return
        if not isBalanced(currentNode):
            root = balance(currentNode)
            root.height = calcHeight(root)
        return


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
    print(*stackSim)
    print(path)
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
    # return pointer to the inserted element's parent
    return parent


# print bst in order
def printBst(root):
    if root:
        printBst(root.left)
        print(root.data, end=' ')
        printBst(root.right)

randomArray = arr_ints.getRandomArray(10000)
sortedArray = arr_ints.getSortedArray(10000)

print('random:', randomArray)
print('sorted:', sortedArray)

# root = insertIter(root, Node(3))
# printBst(root)
# print()
#
# insertIter(root, Node(1))
# printBst(root)
# print()
#
# insertIter(root, Node(2))
# printBst(root)
# print()
#
# insertIter(root, Node(4))
# printBst(root)
# print()
#
# insertIter(root, Node(7))
# printBst(root)
# print()
#
# insertIter(root, Node(9))
# printBst(root)
# print()
#
# print('root: ', root.data)
#
# deleteIter(root, Node(4))
# printBst(root)
# print()
#
# print('root: ', root.data)
#
# insertIter(root, Node(10))
# printBst(root)
# print()
# insertIter(root, Node(-1))
# printBst(root)
# print()
#
# print('root: ', root.data)
#
# insertIter(root, Node(11))
# printBst(root)
# print()
#
# print('root: ', root.data)
#
# insertIter(root, Node(-2))
# printBst(root)
# print()
#
# print('root: ', root.data)
#
# deleteIter(root, Node(-2))
# printBst(root)
# print()
#
# print('root: ', root.data)
#
# deleteIter(root, Node(-1))
# printBst(root)
# print()
#
# print('root: ', root.data)
#
# deleteIter(root, Node(2))
# printBst(root)
# print()
#
# print('root: ', root.data)
