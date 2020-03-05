# Extra Credit
# 7.a.
# Use the code from ../extracredit_credit(7).py
print('\n\nPart 7.a. --- Extra Credit')
print('----------Random Array----------')
randomArray = arr_ints.getRandomArray(10000)

startBst = time.time()

bst.root = bst.insertIter(None, bst.Node(randomArray[0]))

for n in randomArray[1:]:
    bst.insertIter(bst.root, bst.Node(n))

for n in randomArray:
    bst.deleteIter(bst.root, bst.Node(n))

bstTime = time.time() - startBst
print("BST random 10000 add and delete time --- %s seconds ---" % (bstTime))

startAvl = time.time()

root = insertIter(None, Node(randomArray[0]))

for n in randomArray[1:]:
    insertIter(root, Node(n))

print()

for n in randomArray:
    root = deleteIter(root, Node(n))

avlTime = time.time() - startAvl
print("AVL random 10000 add and delete time --- %s seconds ---" % (avlTime))
print()
print("avl is ",(abs(avlTime - bstTime) / avlTime) * 100.0, "% slower than bst")

print('\n')
print('----------Sorted Array----------')

sortedArray = arr_ints.getSortedArray(10000)

startBst = time.time()

bst.root = bst.insertIter(None, bst.Node(sortedArray[0]))

for n in sortedArray[1:]:
    bst.insertIter(bst.root, bst.Node(n))

for n in sortedArray:
    bst.deleteIter(bst.root, bst.Node(n))

bstTime = time.time() - startBst
print("BST sorted 10000 add and delete time --- %s seconds ---" % (bstTime))


startAvl = time.time()

root = insertIter(None, Node(sortedArray[0]))

for n in sortedArray[1:]:
    insertIter(root, Node(n))

print()

for n in sortedArray:
    root = deleteIter(root, Node(n))

avlTime = time.time() - startAvl
print("AVL sorted 10000 add and delete time --- %s seconds ---" % (avlTime))
print()
print("bst is ",(abs(bstTime - avlTime) / bstTime) * 100.0, "% slower than avl")