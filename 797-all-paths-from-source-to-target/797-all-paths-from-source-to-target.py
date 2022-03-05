class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        nodes = len(graph)
        def findPaths(node,path):
            path.append(node)
            if node == nodes-1:
                pathList.append(path)
            for n in graph[node]:
                currPath = [p for p in path]
                findPaths(n,currPath) 
        pathList = []
        findPaths(0,[])
        return pathList
#         paths = []
#         visited = [False]*len(graph)
#         def DFS(graph, src, dest, path):
#             visited[src] = True
#             path.append(src)
            
#             if src == dest:
#                 paths.append(path[:])
#             else:
#                 for node in graph[src]:
#                     if not visited[node]:
#                         DFS(graph, node, dest, path)

#             path.pop()
#             visited[src] = False
        
#         DFS(graph, 0, len(graph)-1, [])
#         return paths