# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## iteration
        # curr = head
        # reversed = None
        # while curr:
        #     temp = curr.next
        #     curr.next = reversed
        #     reversed = curr
        #     curr = temp
        # return dummy
        
        ## recursion
        if head is None or head.next is None:
            return head
        p = ListNode()
        p = self.reverseList(head.next)
        # temporarily we make it cycle
        head.next.next = head
        head.next = None
        return p
        
        