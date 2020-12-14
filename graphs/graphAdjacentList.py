#graph using adjacent list
#undirected

class graphAL:
  def __init__(self):
    self.noofnodes = 0
    self.adjacentList = {}

  def addVertex(self,node):
    self.adjacentList[node] = []
    self.noofnodes += 1

  def addEdge(self,node1, node2):
    self.adjacentList[node1].append(node2)
    self.adjacentList[node2].append(node1)

  def showConnections(self):
    for node, edgelist in self.adjacentList.items():
      nodeAndEdges = ""
      nodeAndEdges = nodeAndEdges + str(node) + " --> " 
      for i in range(len(edgelist)):
        nodeAndEdges = nodeAndEdges + str(edgelist[i]) + " "
      print(nodeAndEdges)
        
  


