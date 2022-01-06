class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UnionFind:
            def __init__(self, size):
                self.root = [i for i in range(size)]
                self.rank = [1] * size

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

        size = len(s)
        charList = [""] * size
        uf = UnionFind(size)
        for pair in pairs:
            uf.union(pair[0],pair[1])

        charMap = defaultdict(list)
        indexMap = defaultdict(list)
        for i in range(size):
            root = uf.find(i)
            charMap[root].append(s[i])
            indexMap[root].append(i)

        for key, val in charMap.items():
            val.sort()
            for i, c in enumerate(val):
                charList[indexMap[key][i]] = c
        return "".join(charList)
        