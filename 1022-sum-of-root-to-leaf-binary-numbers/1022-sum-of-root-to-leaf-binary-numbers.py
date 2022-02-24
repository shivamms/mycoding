# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ## recursion
        
        # node = root
        # self.treeSum = 0
        # def rootToLeaf(node, number):
        #     if node:
        #         number = (number << 1) | node.val
        #         if node.left is None and node.right is None:
        #             self.treeSum += number
        #         rootToLeaf(node.left, number)
        #         rootToLeaf(node.right, number)
        # rootToLeaf(node, 0)
        # return self.treeSum
        
        ## iteration
        node = root
        number = treeSum = 0
        stack = [(node, number)]
        while stack:
            node, number = stack.pop()
            if node:
                number = (number << 1) | node.val
                if node.left is None and node.right is None:
                    treeSum += number
                else:
                    stack.append((node.left, number))
                    stack.append((node.right, number))
        return treeSum
        