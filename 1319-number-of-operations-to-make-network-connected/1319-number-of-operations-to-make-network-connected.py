class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, size):
                self.root = [i for i in range(size)]
                self.size = size
                self.cables = n
                
            def find(self, x):
                if self.root[x] == x:
                    return x
                self.root[x] = self.find(self.root[x])
                return self.root[x]
            
            def union(self, x,y):
                rootx = self.find(x)
                rooty = self.find(y)
                if rootx != rooty:
                    self.root[rooty] = rootx
                    self.cables -= 1
                # else:
                #     self.cables += 1
            
        uf = UnionFind(n)
        for conn in connections:
            uf.union(conn[0],conn[1])
        if len(connections) >= n-1:
            return uf.cables-1 
        return -1
    
        # roots = set()
        # for i in range(n):
        #     roots.add(uf.find(i))
        # if len(roots)-1 == uf.cables:
        #     return uf.cables
        # elif len(roots)-1 > uf.cables:
        #     return -1
        # elif len(roots)-1 < uf.cables:
        #     return len(roots)-1
        
        