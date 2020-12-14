
import graphs.graphAdjacentList as gal

mygraph = gal.graphAL()
mygraph.addVertex('0')
mygraph.addVertex('1')
mygraph.addVertex('2')
mygraph.addVertex('3')
mygraph.addVertex('4')
mygraph.addVertex('5')
mygraph.addVertex('6')

mygraph.addEdge('0','1')
mygraph.addEdge('0','2')
mygraph.addEdge('1','3')
mygraph.addEdge('2','1')
mygraph.addEdge('3','4')
mygraph.addEdge('4','2')
mygraph.addEdge('4','5')
mygraph.addEdge('5','6')

mygraph.showConnections()

