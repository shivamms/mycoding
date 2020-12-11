class node:
  def __init__(self,val=None):
    self.value = val
    self.next = None

class queue:
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0

  def enqueue(self,item):
    place = node(item)
    if self.length == 0:
      self.first = place
      self.last = place
      self.first.next = self.last
    else:
      self.last.next = place
      self.last = place
    self.length += 1

  def dequeue(self):
    if self.length > 0:
      temp = self.first
      self.first = temp.next
      self.length -= 1
      return temp.value

  def peek(self):
    if self.length > 0:
      return self.first.value

  def display(self):
    item = self.first
    for i in range(self.length):
      print(item.value)
      item = item.next