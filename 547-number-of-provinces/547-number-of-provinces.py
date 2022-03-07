class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        ## using UnionFind
#         class UnionFind:
#             def __init__(self, size):
#                 self.root = [i for i in range(size)]
                
#             def find(self, x):
#                 while self.root[x] != x:
#                     x = self.root[x]
#                 return x
            
#             def union(self, x,y):
#                 rootx = self.find(x)
#                 rooty = self.find(y)
#                 if rootx != rooty:
#                     self.root[rooty] = rootx
                    
#             def connected(self, x,y):
#                 return find(x) == find(y)
        
#         provinces = set()
#         n = len(isConnected)
#         uf = UnionFind(n)
#         for r in range(n):
#             for c in range(n):
#                 if isConnected[r][c]:
#                     uf.union(r,c)
            
#         for r in range(n):
#             provinces.add(uf.find(r))
#         return len(provinces)
    
        ## DFS
#         n = len(isConnected)
#         visited = set()
#         def dfs(r):
#             for c in range(n):
#                 if c not in visited and isConnected[r][c] == 1:
#                     visited.add(c)
#                     dfs(c)

#         count = 0;
#         for r in range(n):
#             if r not in visited:
#                 dfs(r)
#                 count += 1
#         return count
        ## BFS
 
        visited,count, queue, n = set(), 0, deque(), len(isConnected)
        for r in range(n):
            if r not in visited:
                queue.append(r)
                while queue:
                    row = queue.pop()
                    visited.add(row)
                    for col in range(n):
                        if isConnected[row][col] == 1 and col not in visited:
                            queue.append(col)
                count += 1
        return count;

                    
            