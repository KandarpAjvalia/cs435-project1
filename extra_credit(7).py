
# Extra credit 7.a. use the below code inside bbst.py to see the results
print('\n\nPart 7.a. --- Extra Credit')
sortedArray = arr_ints.getsortedArray(200000)

startBst = time.time()

bst.root = bst.insertIter(None, bst.Node(sortedArray[0]))

for n in sortedArray[1:]:
    bst.insertIter(bst.root, bst.Node(n))

for n in sortedArray:
    bst.deleteIter(bst.root, bst.Node(n))

bstTime = time.time() - startBst
print("BST 200000 add and delete time --- %s seconds ---" % (bstTime))


startAvl = time.time()

root = insertIter(None, Node(sortedArray[0]))

for n in sortedArray[1:]:
    insertIter(root, Node(n))

print()

for n in sortedArray:
    root = deleteIter(root, Node(n))

avlTime = time.time() - startAvl
print("AVL 200000 add and delete time --- %s seconds ---" % (avlTime))
print()
print("Avl is ",(abs(avlTime - bstTime) / avlTime) * 100.0, "% slower than bst")



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