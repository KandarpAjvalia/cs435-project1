import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

root = None


def insertRec(currentNode, nodeToInsert):
    if currentNode is None:
        return nodeToInsert
    if nodeToInsert.data < currentNode.data:
        currentNode.left = insertRec(currentNode.left, nodeToInsert)
    else:
        currentNode.right = insertRec(currentNode.right, nodeToInsert)
    return currentNode


def insertIter(root, nodeToInsert):
    curr = root
    parent = None
    insertData = nodeToInsert.data

    while curr is not None:
        currData = curr.data
        parent = curr
        if insertData < currData:
            curr = curr.left
        else:
            curr = curr.right

    if parent is None:
        parent = nodeToInsert

    elif insertData < parent.data:
        parent.left = nodeToInsert
    else:
        parent.right = nodeToInsert

    return parent

def deleteRec(currentNode, nodeToDelete):
    if currentNode is None:
        return currentNode

    deleteData = nodeToDelete.data
    currData = currentNode.data

    if deleteData < currData:
        currentNode.left = deleteRec(currentNode.left, nodeToDelete)
    elif deleteData > currData:
        currentNode.right = deleteRec(currentNode.right, nodeToDelete)
    else:
        if currentNode.right is None:
            update = currentNode.left
            currentNode = None
            return update
        elif currentNode.left is None:
            update = currentNode.right
            currentNode = None
            return update

        leftMost = currentNode.right
        while leftMost.left is not None:
            leftMost = leftMost.left
        update = leftMost
        currentNode.data = update.data
        currentNode.right = deleteRec(currentNode.right, Node(update.data))

    return currentNode

def deleteIter(currentNode, nodeToDelete):
    parent = None
    global root
    if currentNode is None:
        return
    elif currentNode.data == nodeToDelete.data:
        if currentNode.left is None and currentNode.right is None:
            currentNode = None
            root = currentNode
        elif currentNode.left and currentNode.right is None:
            currentNode = currentNode.left
            root = currentNode
        elif currentNode.left is None and currentNode.right:
            currentNode = currentNode.right
            root = currentNode
        elif currentNode.left and currentNode.right:
            parent = currentNode
            tempNode = currentNode.right
            while tempNode.left:
                parent = tempNode
                tempNode = tempNode.left
            currentNode.data = tempNode.data
            if tempNode.right:
                if tempNode.data < parent.data:
                    parent.left = tempNode.right
                elif tempNode.data > parent.data:
                    parent.right = tempNode.right
            else:
                if tempNode.data < parent.data:
                    parent.left = None
                else:
                    parent.right = None

        return

    temp = currentNode

    deletionData = nodeToDelete.data
    while temp and temp.data != deletionData:
        parent = temp
        if deletionData < temp.data:
            temp = temp.left
        elif deletionData > temp.data:
            temp = temp.right

    if temp is None or temp.data != deletionData:
        pass

    elif temp.left is None and temp.right is None:
        if deletionData < parent.data:
            parent.left = None
        else:
            parent.right = None

    elif temp.left and temp.right is None:
        if deletionData < parent.data:
            parent.left = temp.left
        else:
            parent.right = temp.left

    elif temp.left is None and temp.right:
        if deletionData < parent.data:
            parent.left = temp.right
        else:
            parent.right = temp.right

    else:
        nodeTarget = temp
        tempNode = temp.right

        while tempNode.left:
            nodeTarget = tempNode
            tempNode = tempNode.left

        temp.data = tempNode.data

        if tempNode.left:
            if tempNode.data < nodeTarget.data:
                nodeTarget.left = None
            else:
                nodeTarget.right = None
        else:
            if tempNode.data < nodeTarget.data:
                nodeTarget.left = tempNode.right
            elif tempNode.data > nodeTarget.data:
                nodeTarget.right = tempNode.right


def findNextRec(currentNode, data, default=None):
    if currentNode is None:
        return

    temp = currentNode
    if currentNode.data == data:
        slider = None
        if temp.right:
            slider = temp.right
            while slider.left:
                slider = slider.left
            return slider
        else:
            return default
    elif data < currentNode.data:
        return findNextRec(currentNode.left, data, default=currentNode)
    else:
        return findNextRec(currentNode.right, data, default=currentNode)


def findNextIter(currentNode, data):
    temp = currentNode
    while temp and temp.data != data:
        if data < temp.data:
            temp = temp.left
        elif data > temp.data:
            temp = temp.right

    slider = None
    if temp.right:
        slider = temp.right
        while slider.left:
            slider = slider.left
        return slider

    while currentNode:
        if temp.data < currentNode.data:
            slider = currentNode
            currentNode = currentNode.left
        elif temp.data > currentNode.data:
            currentNode = currentNode.right
        else:
            break

    return slider


def findPrevRec(currentNode, data, default=None):
    if currentNode is None:
        return

    temp = currentNode
    if currentNode.data == data:
        slider = None
        if temp.left:
            slider = temp.left
            while slider.right:
                slider = slider.right
            return slider
        else:
            return default
    elif data < currentNode.data:
        return findPrevRec(currentNode.left, data, default=currentNode)
    else:
        return findPrevRec(currentNode.right, data, default=currentNode)


def findPrevIter(currentNode, data):
    if currentNode is None:
        return currentNode

    prevNode = None
    temp = currentNode
    while temp and temp.data != data:
        if data < temp.data:
            temp = temp.left
        elif data > temp.data:
            prevNode = temp
            temp = temp.right

    if temp and temp.left:
        slider = temp.left
        while slider.right:
            slider = slider.right
        return slider
    return prevNode

def findMinRec(currentNode):
    if currentNode is None:
        return sys.maxsize
    return min(currentNode.data, findMinRec(currentNode.left), findMinRec(currentNode.right))


def findMinIter(currentNode):
    if currentNode is None:
        return currentNode
    temp = currentNode
    while temp.left:
        temp = temp.left
    return temp.data


def findMaxRec(currentNode):
    if currentNode is None:
        return -sys.maxsize
    return max(currentNode.data, findMaxRec(currentNode.left), findMaxRec(currentNode.right))


def findMaxIter(currentNode):
    if currentNode is None:
        return currentNode
    temp = currentNode
    while temp.right:
        temp = temp.right
    return temp.data


def printBst(root):
    if root:
        printBst(root.left)
        print(root.data, end=' ')
        printBst(root.right)


# root = insertIter(root, Node(1))
# insertIter(root, Node(3))
# insertIter(root, Node(4))
# insertIter(root, Node(5))
# insertIter(root, Node(6))
# insertIter(root, Node(2))
# insertIter(root, Node(8))
#
# printBst(root)
# print()
#
# deleteIter(root, Node(2))
# printBst(root)
# print()
#
# deleteIter(root, Node(1))
# printBst(root)
# print()
#
# deleteIter(root, Node(6))
# printBst(root)
# print()
#
#
# print('min Rec', findMinRec(root))
# print('max Rec', findMaxRec(root))
#
# print('min Iter', findMinIter(root))
# print('max Iter', findMaxIter(root))
#
# print('next iter', findNextIter(root, 5).data)
# print('next Rec', findNextRec(root, 5).data)
#
# print('prev rec', findPrevRec(root, 4).data)
# print('prev iter', findPrevIter(root, 4).data)