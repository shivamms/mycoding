class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        class UnionFind:
            def __init__(self,n):
                self.root = [i for i in range(n)]

            def find(self, x):
                while self.root[x] != x:
                    x = self.root[x]
                return x

            def union(self, x,y):
                rootx = self.find(x)
                rooty = self.find(y)
                if rootx != rooty:
                    self.root[rooty] = rootx

            def allAcq(self):
                rootnode = self.find(0)
                for i in range(1,n):
                    if rootnode != self.find(i):
                        return False
                return True

        logs.sort()
        uf = UnionFind(n)
        for l in logs:
            uf.union(l[1],l[2])
            if uf.allAcq():
                return l[0]
        return -1
        