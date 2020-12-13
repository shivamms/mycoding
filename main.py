import trees.binarySearchTree as bst
import json

#        10
#       7   24
#.    1       102
tree = bst.btree()
tree.insert(20)
tree.insert(24)
tree.insert(1)
tree.insert(7)
tree.insert(18)
tree.insert(102)

print(tree.lookup(6))
print(tree.remove(102))
print(tree.lookup(102))
print(tree.remove(7))
print(tree.lookup(7))
print(tree.remove(7))
#print(json.dumps(str(tree.root)))

#tree.printTree(tree.root)
