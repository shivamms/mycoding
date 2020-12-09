class node:
  def __init__(self,val=None):
    self.value = val
    self.next = None

class stack:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0

  def push(self,item):
    place = node(item)
    if self.length == 0:
      self.top = place
      self.bottom = place
      self.top.next = self.bottom
    else:
      temp = self.top
      self.top = place
      self.top.next = temp
    self.length += 1

  def pop(self):
    if self.length > 0:
      temp = self.top
      self.top = temp.next
      self.length -= 1
      return temp.value

  def peek(self):
    if self.length > 0:
      return self.top.value

  def display(self):
    item = self.top
    for i in range(self.length):
      print(item.value)
      item = item.next

class stackArray:
  def __init__(self):
    self.stack = []
    self.top = None
    self.bottom = None
    self.length = 0

  def push(self,item):
    self.stack.append(item)
    self.length += 1
    if self.length == 0:
      self.top = self.stack[0]
      self.bottom = self.stack[0]
    else:
      self.top = self.stack[self.length-1]

  def pop(self):
    if self.length > 0:
      item = self.stack.pop()
      self.length -= 1
      if len(self.stack) > 0:
        self.top = self.stack[self.length-1]
      return item

  def peek(self):
    if self.length > 0:
      return self.stack[self.length-1]

  def display(self):
    for i in range(self.length-1,-1,-1):
      print(self.stack[i])
      

