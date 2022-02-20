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
            if m == n and m > 0:
                return node
            n += 1
            node = node.next
            if node is None:
                m, n = (n // 2) + 1, 1
                node = head

        