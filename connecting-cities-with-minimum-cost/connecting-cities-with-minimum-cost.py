class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        djs = DisjointSet(n)
        
        connections.sort(key = lambda conn: conn[2])

        mstCost = 0
        count = 0
        for conn in connections:
            either = conn[0]
            other = conn[1]
            if not djs.connected(either, other):
                djs.union(either, other)
                mstCost += conn[2]
                count += 1
        if count == n -1:
            return mstCost
        else:
            return -1

class DisjointSet:
    def __init__(self, n):
        self.parents = [i for i in range(n+1)]
        self.weights = [1 for i in range(n+1)] 

    def find(self, either):
        while either != self.parents[either]:
            self.parents[either] = self.find(self.parents[self.parents[either]])
            either = self.parents[either]
        return self.parents[either]
    
    def union(self, either, other):
        nodeA = self.find(either)
        nodeB = self.find(other)
        if nodeA == nodeB: return
        
        if self.weights[nodeA] > self.weights[nodeB]:
            self.parents[nodeB] = nodeA
            self.weights[nodeA] += self.weights[nodeB]
        else:
            self.parents[nodeA] = nodeB
            self.weights[nodeB] += self.weights[nodeB]

    def connected(self, either, other):
        return self.find(either) == self.find(other)
