"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:  
## DFS - Recursion
#         output = []
#         def dfs(node):
#             if node is None: return
#             output.append(node.val)
#             for node in node.children:
#                 dfs(node)
        
#         node = root
#         dfs(node)
#         return output

## Iteration
        if root is None:
            return []
        node = root
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            stack.extend(root.children[::-1])
        return output
                
        
        