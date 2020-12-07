class node:
  def __init__(self,val=None):
    self.value = val
    self.next = None

class linkedlist:
  def __init__ (self,node):
    self.head = node
    self.tail = node
    self.tail.next = None

  def prepend(self, node):
    node.next = self.head
    self.head = node
  
  def append(self, node):
    self.tail.next = node
    self.tail = node
    self.tail.next = None

  def insertafter(self, existingnode, newnode):
    nextnode = existingnode.next
    existingnode.next = newnode
    newnode.next = nextnode

  def insertbefore(self, existingnode, newnode):
    node = self.head
    while 1:
      if node.value == existingnode.value:
        previousnode.next = newnode
        newnode.next = existingnode
        break
      previousnode = node
      node = node.next

  def display(self):
    node = self.head
    while 1:
      print(node.value)
      if node.next is None:
        break
      node = node.next








