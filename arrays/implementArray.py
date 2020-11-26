class arr:
  def __init__(self):
    self.data = {}
    self.length = 0
  
  def push(self,item):
    self.data[self.length] = item
    self.length += 1
    return self.length

  def pop(self):
    del self.data[self.length-1]
    self.length -= 1
    return self.length

#optional - we can add a method to display the data value in the form of list i.e. []
def createarray():
  myarr = arr()
  myarr.push(1)
  myarr.push('a')
  myarr.push(0.5)
  myarr.push('b')
  print(myarr.data)
  print(myarr.length)
  myarr.pop()
  myarr.pop()
  print(myarr.data)
  print(myarr.length)  
  return myarr
