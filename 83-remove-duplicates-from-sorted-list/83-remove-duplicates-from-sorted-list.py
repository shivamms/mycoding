# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(-101)
        dummy.next = head
        curr = dummy.next
        while curr:
            if curr.next and curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next