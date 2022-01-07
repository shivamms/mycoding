class Solution:
    from collections import defaultdict
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        class UnionFind:
            def __init__(self):
                self.disj = defaultdict(dict)

            def find(self,x):
                if x not in self.disj:
                    self.disj[x] = (x, 1)
                node, weight = self.disj[x]
                if node != x:
                    node, new_weight = self.find(node)
                    self.disj[x] = (node, weight * new_weight)
                return self.disj[x]

            def union(self, x, y, weight):
                dvnd, dvnd_weight = self.find(x)
                dvsr, dvsr_weight = self.find(y)
                if dvnd != dvsr:
                    self.disj[dvnd] = (dvsr, dvsr_weight * weight / dvnd_weight)

        uf = UnionFind()
        for i, e in enumerate(equations):
            uf.union(e[0], e[1], values[i])
        print(uf.disj)

        queryVals = []
        for dvnd, dvsr in queries:
            if dvnd not in uf.disj or dvsr not in uf.disj:
                    queryVals.append(-1.0)
            else:
                dvnd, dvnd_weight = uf.find(dvnd)
                dvsr, dvsr_weight = uf.find(dvsr)
                if dvnd != dvsr:
                    queryVals.append(-1.0)
                else:
                    queryVals.append(dvnd_weight / dvsr_weight)
        return queryVals
        