class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        class UnionFind:
            def __init__(self, size):
                self.root = [i for i in range(size)]
                self.rank = [1] * size
                self.loop = False

            def find(self, x):
                if self.root[x] == x:
                    return x
                self.root[x] = self.find(self.root[x])
                return self.root[x]

            def union(self, x, y):
                rootx = self.find(x)
                rooty = self.find(y)
                if rootx != rooty:
                    if self.rank[rootx] > self.rank[rooty]:
                        self.root[rooty] = rootx
                    elif self.rank[rooty] > self.rank[rootx]:
                        self.root[rootx] = rooty 
                    else:
                        self.root[rooty] = rootx
                        self.rank[rootx] += 1
                elif rootx == rooty and x != y:
                    self.loop = True
        
        if n == 1:
            return True
        if len(edges) < n - 1:
            return False
        uf = UnionFind(n)
        rootVals = set()
        for e in edges:
            uf.union(e[0],e[1])
            if uf.loop:
                return False
        for e in edges:
            rootVals.add(uf.find(e[0]))
            rootVals.add(uf.find(e[1]))
        return len(rootVals) == 1