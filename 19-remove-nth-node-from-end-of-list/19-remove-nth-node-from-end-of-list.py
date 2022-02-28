# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        following = forward = dummy
        i = 1
        while i <= n+1:
            i += 1
            forward = forward.next
        while forward:
            following = following.next
            forward = forward.next
        following.next = following.next.next
        return dummy.next
        