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
        if root is None:
            return None
        dq = deque([(root, None)])
        while dq:
            nodes = dq.popleft()
            nodes[0].next = nodes[1]
            if nodes[1]:
                nodes[1].next = None
            if nodes[0].left:
                dq.append((nodes[0].left,nodes[0].right))
            if nodes[1] and nodes[1].left:
                dq.append((nodes[0].right,nodes[1].left))
                dq.append((nodes[1].left,nodes[1].right))
        return root