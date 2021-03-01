#import graphs.AdjacentList as gal
import wayfair_has_common_ancestor as hca

# mygraph = gal.graphAL()
# mygraph.addVertex('0')
# mygraph.addVertex('1')
# mygraph.addVertex('2')
# mygraph.addVertex('3')
# mygraph.addVertex('4')
# mygraph.addVertex('5')
# mygraph.addVertex('6')

# mygraph.addEdge('0','1')
# mygraph.addEdge('0','2')
# mygraph.addEdge('1','3')
# mygraph.addEdge('2','1')
# mygraph.addEdge('3','4')
# mygraph.addEdge('4','2')
# mygraph.addEdge('4','5')
# mygraph.addEdge('5','6')

# mygraph.showConnections()

parent_child_pairs_1 = [
    (1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5),
    (4, 8), (4, 9), (9, 11), (14, 4), (13, 12), (12, 9),
    (15, 13)
]

parent_child_pairs_2 = [
    (1, 3), (11, 10), (11, 12), (2, 3), (10, 2), 
    (10, 5), (3, 4), (5, 6), (5, 7), (7, 8)
]

print(hca.has_common_ancestor(parent_child_pairs_2, 4, 12))