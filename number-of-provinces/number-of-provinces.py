class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, size):
                self.root = [i for i in range(size)]
                self.rank = [1] * size
                self.count = size

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
                    self.count -= 1
                print(self.root)

            def getCount(self):
                return self.count

        rows = len(isConnected)
        cols = len(isConnected[0])
        uf = UnionFind(rows)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    uf.union(i,j)

        return uf.getCount()
        