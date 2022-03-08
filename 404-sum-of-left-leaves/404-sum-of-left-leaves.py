# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        node = root
        leftNodesSum = 0
        def leftSum(node, isLeft):
            if node is None:
                return 0
            if node.left is None and node.right is None:
                return node.val if isLeft else 0
            return leftSum(node.left, True) + leftSum(node.right, False)

        return leftSum(node, False)