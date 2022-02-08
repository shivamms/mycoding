# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.sorted_nodes = []
        self.pointer = -1
        self.flatten(root)
        self.size = len(self.sorted_nodes)
        
    def flatten(self, node):
        if node is None:
            return
        self.flatten(node.left)
        self.sorted_nodes.append(node.val)
        self.flatten(node.right)
        
    def next(self) -> int:
        if self.pointer < len(self.sorted_nodes)-1:
            self.pointer += 1
            return self.sorted_nodes[self.pointer]

    def hasNext(self) -> bool:
        return self.pointer < len(self.sorted_nodes)-1


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()