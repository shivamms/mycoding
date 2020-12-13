

class btreenode:
  def __init__(self,value):
    self.left = None
    self.right = None
    self.value = value

class btree:
  def __init__(self):
    self.root = None

  def insert(self,value):
    newnode = btreenode(value)
    if self.root is None:
      self.root = newnode
    else:
      node = self.root
      while True:
        if value < node.value:
          if node.left is None:
            node.left = newnode
            return None
          node = node.left
        else:
          if node.right is None:
            node.right = newnode
            return None
          node = node.right
      
  def lookup(self,value):
    currentnode = self.root
    while currentnode is not None:
      if currentnode.value == value:
        return True
      elif currentnode.value > value:
        currentnode = currentnode.left
      elif currentnode.value <= value:
        currentnode = currentnode.right
    return False

  def remove(self,value):
    if self.root is None:
      return False
    currentnode = self.root
    parentnode = None
    while currentnode is not None:
      if currentnode.value > value:
        parentnode = currentnode
        currentnode = currentnode.left
      elif currentnode.value < value:
        parentnode = currentnode
        currentnode = currentnode.right
      elif currentnode.value == value:
        if currentnode.right is None:
          if parentnode is None:
            self.root = currentnode.left
          else:
            if currentnode.value < parentnode.value:
              parentnode.left = currentnode.left
            elif currentnode.value > parentnode.value:
              parentnode.right = currentnode.left
        elif currentnode.right.left is None:
          currentnode.right.left = currentnode.left
          if parentnode is None:
            self.root = currentnode.right
          else:
            if currentnode.value < parentnode.value:
              parentnode.left = currentnode.right
            elif currentnode.value > parentnode.value:
              parentnode.right = currentnode.right
        else:
          #find the Right child's left most child
          leftmost = currentnode.right.left;
          leftmostparent = currentnode.right;
          while leftmost.left is not None:
            leftmostparent = leftmost
            leftmost = leftmost.left
          #Parent's left subtree is now leftmost's right subtree
          leftmostparent.left = leftmost.right;
          leftmost.left = currentnode.left;
          leftmost.right = currentnode.right;

          if parentnode is None:
            self.root = leftmost
          else:
            if currentnode.value < parentnode.value:
              parentnode.left = leftmost
            elif currentnode.value > parentnode.value:
              parentnode.right = leftmost
      return True


        


