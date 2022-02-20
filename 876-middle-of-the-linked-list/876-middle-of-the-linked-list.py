# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = m = 0
        node = head
        while node:
            n += 1
            node = node.next
        m, n = (n // 2) + 1, 0
        node = head
        while node:
            n += 1
            if n == m:
                return node
            node = node.next
        