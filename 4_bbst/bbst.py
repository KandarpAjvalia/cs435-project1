import sys

# creating a structure of node
class Node:
    def __init__(self, data):
        self.data = data
        self.height = 1
        self.left = None
        self.right = None

# Initializing root as null
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

    # if root is none, return pointer to the given node
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


# print bst in order
def printBst(root):
    if root:
        printBst(root.left)
        print(root.data, end=' ')
        printBst(root.right)


root = insertIter(root, Node(3))
printBst(root)
print()

insertIter(root, Node(1))
printBst(root)
print()

insertIter(root, Node(2))
printBst(root)
print()

insertIter(root, Node(4))
printBst(root)
print()

insertIter(root, Node(7))
printBst(root)
print()

insertIter(root, Node(9))
printBst(root)
print()

insertIter(root, Node(3))
printBst(root)
print()

insertIter(root, Node(3))
printBst(root)
print()

insertIter(root, Node(3))
printBst(root)
print()

print('root: ', root.data)