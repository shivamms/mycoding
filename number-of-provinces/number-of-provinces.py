from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(isConnected, visited, i):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and visited[j] == 0: 
                    visited[j] = 1 
                    dfs(isConnected, visited, j) 

        length = len(isConnected)
        visited = [0] * length
        count = 0
        for i in range(length):
            if visited[i] == 0: 
                dfs(isConnected, visited, i) 
                count += 1
        return count
    
#Notes:
# 1. Make use of the given matrix as adjacent matrix.
# 2. The whole input data structure is undirected graph.
# 3. Index of each row in the matrix represents one node of the graph.
# 4. Each 1 in the row represents the connection between the node in the row index and the node in the column index.
# 5. Since the data structure is undirected graph, treat each node as root node and do a DFS from each node (N * DFS where N is number of nodes).
# 6. Maintain a list of visited nodes, while doing DFS, make an entry in visited nodes list whenever we visit a node.
# 7. Understand that for a DFS from any first node from a group of connected nodes, we get one province. Visits (DFS) from other nodes in the same province are ignored. Since we visit every node in a province (connected nodes). we complete visiting all the nodes in the province. So if we found a node already in the visited list, it means, it is part of some province and we do not need to count it.

        