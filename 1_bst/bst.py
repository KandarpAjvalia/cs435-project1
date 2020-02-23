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


def insertIter(root, nodeToInsert):
    if root is None:
        root = nodeToInsert
        return root

    curr = root
    parent = None

    currData = curr.data
    insertData = nodeToInsert.data
    left = False

    while curr is not None:
        left = False
        parent = curr
        if insertData < currData:
            curr = curr.left
            left = True
        else:
            curr = curr.right

    if left:
        parent.left = nodeToInsert
    else:
        parent.right = nodeToInsert

    return parent


def printBst(root):
    if root:
        printBst(root.left)
        print(root.data)
        printBst(root.right)


# rootRec = None
# temp = Node(10)
# rootRec = insertRec(rootRec, temp)
# insertRec(rootRec, Node(1))
# insertRec(rootRec, Node(100))
# printBst(rootRec)

# rootIter = None
# temp = Node(10)
# rootIter = insertIter(rootIter, temp)
# insertIter(rootIter, Node(1))
# insertIter(rootIter, Node(100))
# printBst(rootIter)