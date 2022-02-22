# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # DFS
        # if root1 is None:
        #     return root2
        # if root2 is None:
        #     return root1
        # root1.val += root2.val
        # root1.left = self.mergeTrees(root1.left, root2.left)
        # root1.right = self.mergeTrees(root1.right, root2.right)
        # return root1
        
        #BFS
        if root1 is None:
            return root2
        stack = []
        stack.append((root1, root2))
        while stack:
            nodes = stack.pop()
            if nodes[0] is None or nodes[1] is None:
                continue
            nodes[0].val += nodes[1].val
            if nodes[0].left is None:
                nodes[0].left = nodes[1].left
            else:
                stack.append((nodes[0].left, nodes[1].left))
            
            if nodes[0].right is None:
                nodes[0].right = nodes[1].right
            else:
                stack.append((nodes[0].right, nodes[1].right))
        return root1
            
        
            
            
        