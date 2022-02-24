# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if head is None or head.next is None: return head
        # p = ListNode()
        # p = self.reverseList(head.next)
        # head.next.next = head
        # head.next = None
        # return p
        prev = None
        curr = head
        while curr:
            temp = ListNode()
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
            
    
        