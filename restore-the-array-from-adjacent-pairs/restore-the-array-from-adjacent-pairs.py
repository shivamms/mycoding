class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjacentList = defaultdict(list)
        for i, p in enumerate(adjacentPairs):
            adjacentList[p[0]].append(p[1])
            adjacentList[p[1]].append(p[0])
        
        start = None          
        for key, val in adjacentList.items(): 
            if len(val) == 1:
                start = key
                break

        nums = []             
        visited = set()
        visited.add(start)
        nums.append(start)
        def dfs(node):
            for n in adjacentList[node]:
                if n not in visited:
                    visited.add(n)
                    nums.append(n)
                    dfs(n)
                    break

        dfs(start)
        return nums
    