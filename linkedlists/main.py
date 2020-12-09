import linkedlists.implementLinkedList as ill

# singly linked list test
mynode = ill.node(14)
nextnode = ill.node(18)
mynode.next = nextnode
thirdnode = ill.node(20)
nextnode.next = thirdnode

node = mynode
while 1:
  print(node.value)
  if node.next is None:
    break
  node = node.next

node0 = ill.node("a")
node1 = ill.node("amma")
node2 = ill.node("aadu")
node3 = ill.node("elai")
mylist = ill.linkedlist(node1)
mylist.append(node2)
mylist.append(node3)
mylist.prepend(node0)

mylist.display()

node0.value = "amma"
node1.value = "aadu"
node2.value = "elai"
node3.value = "eli"
node4 = ill.node("Iaindu")
mylist.append(node4)

mylist.display()

node22 = ill.node("eee")
node33 = ill.node("aeni")

mylist.insertafter(node2,node22)
mylist.display()

mylist.insertbefore(node4,node33)
mylist.display()

node8 = ill.node("ottagam")
mylist.insertByIndex(7,node8)
mylist.display()

node9 = ill.node("avvaiyar")
mylist.insertByIndex(8,node9)
mylist.display()

node10 = ill.node("oonai")
mylist.insertByIndex(8,node10)
mylist.display()
print(mylist.length)

"""
# doubly linked list test
mynode = ill.node(14)
nextnode = ill.node(18)
mynode.next = nextnode
thirdnode = ill.node(20)
nextnode.next = thirdnode

node = mynode
while 1:
  print(node.value)
  if node.next is None:
    break
  node = node.next

node0 = ill.node("a")
node1 = ill.node("amma")
node2 = ill.node("aadu")
node3 = ill.node("elai")
mylist = ill.dlinkedlist(node1)
mylist.append(node2)
mylist.append(node3)
mylist.prepend(node0)

mylist.display()

node0.value = "amma"
node1.value = "aadu"
node2.value = "elai"
node3.value = "eli"
node4 = ill.node("Iaindu")
mylist.append(node4)

mylist.display()

node22 = ill.node("eee")
node33 = ill.node("aeni")

mylist.insertafter(node2,node22)
mylist.display()

mylist.insertbefore(node4,node33)
mylist.display()

node8 = ill.node("ottagam")
mylist.insertByIndex(7,node8)
mylist.display()

node9 = ill.node("avvaiyar")
mylist.insertByIndex(8,node9)
mylist.display()

node10 = ill.node("oonai")
mylist.insertByIndex(8,node10)
mylist.display()
print(mylist.length)
"""
mylist.reverse()
mylist.display()
mylist.reverse()
mylist.display()






