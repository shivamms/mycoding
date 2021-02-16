class Solution:
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        adjacent_list = defaultdict(list)
        for course, preq in prerequisites:
            adjacent_list[preq].append(course)
        topological_sorted_order = []
        is_possible = True
        visitstatus = {k: "no" for k in range(numCourses)}

        def dfs(node):
            nonlocal is_possible
            if not is_possible:
                return
            visitstatus[node] = "yes"
            if node in adjacent_list:
                for neighbor in adjacent_list[node]:
                    if visitstatus[neighbor] == "no":
                        dfs(neighbor)
                    elif visitstatus[neighbor] == "yes":
                        is_possible = False
            visitstatus[node] = "end"
            topological_sorted_order.append(node)
        for course in range(numCourses):
            if visitstatus[course] == "no":
                dfs(course)
        return topological_sorted_order[::-1] if is_possible else []

        
        
            
            