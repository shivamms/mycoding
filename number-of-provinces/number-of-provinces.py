from collections import defaultdict
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(isConnected, visited, i):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1 and visited[j] == 0: 
                    visited[j] = 1 # [1,0,0]   [1,1,0]
                    dfs(isConnected, visited, j) # [[1,1,0],[1,1,0],[0,0,1]], [1,1,0], 1

        length = len(isConnected)
        visited = [0] * length
        count = 0
        for i in range(length):
            if visited[i] == 0: # [0,0,0]
                dfs(isConnected, visited, i) # [[1,1,0],[1,1,0],[0,0,1]], [0,0,0], 0
                count += 1
        return count
        