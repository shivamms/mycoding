class node:
  def __init__(self,val=None):
    self.value = val
    self.next = None

class linkedlist:
  def __init__ (self,node):
    self.head = node
    self.tail = node
    self.tail.next = None
    self.length = 1

  def prepend(self, node):
    oldheadnode = self.head
    self.head = node
    self.head.next = oldheadnode
    self.length += 1
  
  def append(self, node):
    self.tail.next = node
    self.tail = node
    self.tail.next = None
    self.length += 1

  def insertafter(self, existingnode, newnode):
    if self.tail.value == newnode.value:
      self.tail = newnode
    nextnode = existingnode.next
    existingnode.next = newnode
    newnode.next = nextnode
    self.length += 1

  def insertbefore(self, existingnode, newnode):
    node = self.head
    previousnode = self.head
    while 1:
      if node.value == existingnode.value:
        previousnode.next = newnode
        newnode.next = existingnode
        self.length += 1
        break
      previousnode = node
      node = node.next
    if self.head.value == newnode.value:
      self.head = newnode

  def insertByIndex(self, index, newnode):
    node = self.head
    if index >= self.length:
      self.tail.next = newnode
      self.tail = newnode
      self.tail.next = None
    else:
      for i in range(index):
          node = node.next
      newnode.next = node.next
      node.next = newnode
    self.length += 1

  def removeByNode(self,delnode):
    if self.head.value == delnode.value:
      self.head = self.head.next
      self.length -= 1
      return
    node = self.head
    previousnode = self.head
    for i in range(self.length):
      if node.value == self.tail.value:
        previousnode.next = None
        self.tail = previousnode
        self.length -= 1
        return
      elif node.value == delnode.value:
        previousnode.next = node.next
        self.length -= 1
        return
      previousnode = node
      node = node.next
  
  def removeByIndex(self,index):
    if index >= self.length:
      return "Index out of range"
    if index == 1:
      self.head = self.head.next
      self.length -= 1
      return
    node = self.head
    previousnode = self.head
    for i in range(index):
      previousnode = node
      node = node.next
    previousnode.next = node.next
    self.length -= 1
    return

  def display(self):
    node = self.head
    llistStr = ""
    for i in range(self.length):
      if i == 0:
        llistStr = str(node.value)
      else: 
        llistStr = llistStr + "-->" + str(node.value)
      node = node.next
    print(llistStr)


class dlinkedlist:
  def __init__ (self,node):
    self.head = node
    self.tail = node
    self.head.prev = None
    self.head.next = self.tail
    self.tail.next = None
    self.tail.prev = self.head
    self.length = 1

  def prepend(self, node):
    self.head.prev = node
    node.next = self.head
    self.head = node
    self.length += 1
  
  def append(self, node):
    node.prev = self.tail
    self.tail.next = node
    self.tail = node
    self.tail.next = None
    self.length += 1

  def insertafter(self, existingnode, newnode):
    nextnode = existingnode.next
    existingnode.next = newnode
    newnode.prev = existingnode
    nextnode.prev = newnode
    newnode.next = nextnode
    self.length += 1
    if self.tail.value == newnode.value:
      self.tail = newnode

  def insertbefore(self, existingnode, newnode):
    previousnode = existingnode.prev
    previousnode.next = newnode
    newnode.prev = previousnode
    newnode.next = existingnode
    self.length += 1
    if self.head.value == newnode.value:
      self.head = newnode

  def insertByIndex(self, index, newnode):
    node = self.head
    if index >= self.length:
      self.tail.next = newnode
      newnode.prev = self.tail
      self.tail = newnode
      self.tail.next = None
    else:
      for i in range(index-1):
          node = node.next
      nextnode = node
      newnode.next = node.next
      newnode.prev = node
      node.next = newnode
      nextnode.prev = newnode
    self.length += 1

  def removeByNode(self,delnode):
    if self.head.value == delnode.value:
      self.head = self.head.next
      self.length -= 1
      return
    node = self.head
    previousnode = self.head
    for i in range(self.length):
      if node.value == self.tail.value:
        previousnode.next = None
        self.tail = previousnode
        self.length -= 1
        return
      elif node.value == delnode.value:
        previousnode.next = node.next
        self.length -= 1
        return
      previousnode = node
      node = node.next
  
  def removeByIndex(self,index):
    if index >= self.length:
      return "Index out of range"
    if index == 1:
      self.head = self.head.next
      self.length -= 1
      return
    node = self.head
    previousnode = self.head
    for i in range(index):
      previousnode = node
      node = node.next
    previousnode.next = node.next
    self.length -= 1
    return

  def display(self):
    node = self.head
    llistStr = ""
    for i in range(self.length):
      if i == 0:
        llistStr = str(node.value)
      else: 
        llistStr = llistStr + "<-->" + str(node.value)
      node = node.next
    print(llistStr)








