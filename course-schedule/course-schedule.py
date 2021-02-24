class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacentList = defaultdict(list)
        for course, preq in prerequisites:
            adjacentList[preq].append(course)
        isPossible = True
        visitStatus = ["no" for k in range(numCourses)]
        print(adjacentList)
        
        
        def dfs(node):
            nonlocal isPossible
            if not isPossible:
                return
            
            visitStatus[node] = "yes"
            if node in adjacentList:
                for neighbour in adjacentList[node]:
                    if visitStatus[neighbour] == "no":
                        dfs(neighbour)
                    elif visitStatus[neighbour] == "yes":
                        isPossible = False
            visitStatus[node] = "end"
        
        for course in range(numCourses):
            if visitStatus[course] == "no":
                dfs(course)
        return isPossible