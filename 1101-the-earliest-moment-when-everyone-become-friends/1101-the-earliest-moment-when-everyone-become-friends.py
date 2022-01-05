class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        class UnionFind:
            def __init__(self,n):
                self.root = [i for i in range(n)]
                self.count = n
                self.timestamp = -1

            def find(self, x):
                while self.root[x] != x:
                    x = self.root[x]
                return x

            def union(self, timestamp, x,y):
                rootx = self.find(x)
                rooty = self.find(y)
                if rootx != rooty:
                    self.root[rooty] = rootx
                    self.count -= 1
                    self.timestamp = timestamp
                if self.count == 1:
                    return True
                return False

            def getTimestamp(self):
                return self.timestamp

        uf = UnionFind(n)
        logs.sort()
        for i, l in enumerate(logs):
            if uf.union(l[0],l[1],l[2]):
                return uf.getTimestamp()
        return -1
        