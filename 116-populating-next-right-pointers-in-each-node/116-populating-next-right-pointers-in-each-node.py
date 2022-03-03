"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        leftMost = root
        while leftMost:
            levelHead = leftMost
            while levelHead:
                if levelHead.left and levelHead.right:
                    levelHead.left.next = levelHead.right
                if levelHead.next and levelHead.next.left and levelHead.next.right:
                    levelHead.right.next = levelHead.next.left
                levelHead = levelHead.next
            leftMost = leftMost.left
        return root
        
            
                
                