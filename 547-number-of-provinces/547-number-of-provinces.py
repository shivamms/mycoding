class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, size):
                self.root = [i for i in range(size)]
                
            def find(self, x):
                while self.root[x] != x:
                    x = self.root[x]
                return x
            
            def union(self, x,y):
                rootx = self.find(x)
                rooty = self.find(y)
                if rootx != rooty:
                    self.root[rooty] = rootx
                    
            def connected(self, x,y):
                return find(x) == find(y)
        
        provinces = set()
        n = len(isConnected)
        uf = UnionFind(n)
        for r in range(n):
            for c in range(n):
                if isConnected[r][c]:
                    uf.union(r,c)
            
        for r in range(n):
            provinces.add(uf.find(r))
        return len(provinces)
        
                    
            