class stackArray:
  def __init__(self):
    self.stack = []
    self.top = None
    self.bottom = None
    self.length = 0

  def push(self,item):
      self.stack.append(item)
      self.length += 1
      self.top = self.stack[self.length-1]
      if self.length == 1:
        self.bottom = self.stack[0]
    
  def pop(self):
    if self.length > 0:
      item = self.stack.pop()
      self.length -= 1
      if self.length > 0:
        self.top = self.stack[self.length-1]
      else:
        self.top = None
        self.bottom = None
      return item

  def peek(self):
    if self.length > 0:
      return self.stack[self.length-1]

  def display(self):
    for i in range(self.length-1,-1,-1):
      print(self.stack[i])
      
class queueWithStack:
  def __init__(self):
    self.stack1 = stackArray()
    self.stack2 = stackArray()
    self.first = None
    self.last = None
    self.length = 0

  def enqueue(self,item):
    self.last = item
    if self.stack1.length == 0:
      self.stack1.push(item)
    else:
      while self.stack1.length > 0:
        value = self.stack1.pop()
        self.stack2.push(value) 
      self.stack1.push(item)
      while self.stack2.length > 0:
        value = self.stack2.pop()
        self.stack1.push(value)
    self.first = self.stack1.peek()
    self.length += 1

  def dequeue(self):
    if self.length > 0:
      value = self.stack1.pop()
      self.first = self.stack1.peek()
      return value

  def peek(self):
    return self.stack1.peek()

  def display(self):
    self.stack1.display()


