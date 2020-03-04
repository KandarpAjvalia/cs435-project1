import sys
import inspect

# creating a structure of node
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Initializing node as null
root = None
stack = []
size = 0
travCount = 0


def incrementTrav():
    global travCount
    travCount += 1


# a function to insert a node in a bst recursively
def insertRec(currentNode, nodeToInsert):

    global size
    # base case if we reach a leaf node
    if currentNode is None:
        # stackSize = len(inspect.stack())
        # print('stack frame depth', stackSize)
        # if size < stackSize:
        #     size = stackSize
        return nodeToInsert

    # recursive step, go left down the tree if node to insert is smaller
    # than current, else go down ro the right if the node to insert is greer
    if nodeToInsert.data < currentNode.data:
        incrementTrav()
        currentNode.left = insertRec(currentNode.left, nodeToInsert)
    else:
        incrementTrav()
        currentNode.right = insertRec(currentNode.right, nodeToInsert)

    # return pointer of parent to the node we reached and inserted
    return currentNode


# a function to insert a node in a bst iteratively
def insertIter(root, nodeToInsert):

    # if node is none, return pointer to the given node
    if root is None:
         return nodeToInsert

    # pointers to keep track of our position in the tree
    curr = root
    parent = None
    insertData = nodeToInsert.data

    # slide down left or right depending on the conditions
    while curr is not None:
        currData = curr.data
        parent = curr
        if insertData < currData:
            curr = curr.left
        else:
            curr = curr.right

        incrementTrav()

    # insert on left if element is smaller than parent,
    # else insert to the right
    if insertData < parent.data:
        parent.left = nodeToInsert
    else:
        parent.right = nodeToInsert

    # return pointer to the inserted element's parent
    return parent


# a function to delete a node from bst recursively
def deleteRec(currentNode, nodeToDelete):

    # base case if we reach a node which is none
    if currentNode is None:
        return currentNode

    deleteData = nodeToDelete.data
    currData = currentNode.data

    # go down left if node is smaller than current
    if deleteData < currData:
        currentNode.left = deleteRec(currentNode.left, nodeToDelete)

    # go down right if node is greater than current
    elif deleteData > currData:
        currentNode.right = deleteRec(currentNode.right, nodeToDelete)

    # if node is same as the one we want to delete
    else:

        # if right of node to be deleted is empty(no children)
        if currentNode.right is None:
            return currentNode.left

        # if left of node to be deleted is empty(no children)
        elif currentNode.left is None:
            return currentNode.right

        # we replace the node to be deleted with the next highest in the bst
        # and then delete the next highest node
        leftMost = currentNode.right
        while leftMost.left is not None:
            leftMost = leftMost.left
        update = leftMost
        currentNode.data = update.data

        # we also delete the next highest node in bst
        currentNode.right = deleteRec(currentNode.right, Node(update.data))

    # return pointer to the node
    return currentNode

def deleteIterHelper(currentNode):
    parent = currentNode
    tempNode = currentNode.right

    # this part may be reduced by using findNext function
    # find next biggest element's parent node
    while tempNode.left:
        parent = tempNode
        tempNode = tempNode.left
    currentNode.data = tempNode.data

    # if next biggest's left is empty but has right children, move child left or right
    if tempNode.right:
        if tempNode.right.data < parent.data:
            parent.left = tempNode.right
        elif tempNode.right.data > parent.data:
            parent.right = tempNode.right

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
        return


    temp = currentNode
    deletionData = nodeToDelete.data

    # if node is not a node, we just slide down to the node we want to delete
    while temp and temp.data != deletionData:
        parent = temp
        if deletionData < temp.data:
            temp = temp.left
        elif deletionData > temp.data:
            temp = temp.right

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


# a recursive function to find the next node greater than a given node
def findNextRec(currentNode, data, default=None):

    #base case when node is null
    if currentNode is None:
        return

    temp = currentNode

    # if we find the node we want to find the next of
    if currentNode.data == data:

        slider = None

        # if right node exists
        # we move right and all the way down left of the right node
        if temp.right:
            slider = temp.right
            while slider.left:
                slider = slider.left
            return slider

        # default is the parent node
        else:
            return default

    # move down left if node > current
    elif data < currentNode.data:
        return findNextRec(currentNode.left, data, default=currentNode)

    # move down right if node > current
    else:
        return findNextRec(currentNode.right, data, default=currentNode)


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


# a recursive function to find the previous node smaller than a given node
def findPrevRec(currentNode, data, default=None):

    #base case when node is null
    if currentNode is None:
        return

    temp = currentNode

    # if we find the node we want to find the next of
    if currentNode.data == data:
        slider = None

        # if left node exists
        # we move left and all the way down right of the left node
        if temp.left:
            slider = temp.left
            while slider.right:
                slider = slider.right
            return slider

        # default is the parent node
        else:
            return default

    # move down left if node > current
    elif data < currentNode.data:
        return findPrevRec(currentNode.left, data, default=currentNode)

    # move down right if node > current
    else:
        return findPrevRec(currentNode.right, data, default=currentNode)


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


# a recursive function to find the min of bst
def findMinRec(currentNode):

    # base case, we reach None we return max size num
    # because we don't want to count this, nullify this result
    if currentNode is None:
        return sys.maxsize

    # keep on spreading the tree, returning min of the three
    # currentNode, its left and its right and at the end we will bubble up
    return min(currentNode.data, findMinRec(currentNode.left), findMinRec(currentNode.right))


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


# a recursive function to find the max of bst
def findMaxRec(currentNode):

    # base case, we reach None we return min size num
    # because we don't want to count this, nullify this result
    if currentNode is None:
        return -sys.maxsize

    # keep on spreading the tree, returning max of the three
    # currentNode, its left and its right and at the end we will bubble up
    return max(currentNode.data, findMaxRec(currentNode.left), findMaxRec(currentNode.right))


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
def printBst(root):
    if root:
        printBst(root.left)
        print(root.data, end=' ')
        printBst(root.right)
