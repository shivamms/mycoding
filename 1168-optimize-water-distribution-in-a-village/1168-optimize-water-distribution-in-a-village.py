class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        class UnionFind:
            def __init__(self, size):
                self.root = [i for i in range(size+1)]
                self.rank = [0] * (size + 1)

            def find(self, x):
                if self.root[x] != x:
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
                    return True
                return False
                print(self.root)
                print(self.rank)

        costs = []
        for i, wellCost in enumerate(wells):
            costs.append((wellCost, 0, i+1))
        for i, pipe in enumerate(pipes):
            costs.append((pipe[2], pipe[0], pipe[1]))
        costs.sort(key=lambda x: x[0])
        totalCost = 0
        uf = UnionFind(n)
        for cost in costs:
            if uf.union(cost[1], cost[2]):
                totalCost += cost[0]
        return totalCost
        