# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        arr = []
        node = head
        while node:
            arr.append(node)
            node = node.next
        size = len(arr)
        if size == n:
            return head.next
        if n == 1:
            arr[size-2].next = None
            return head
        arr[size-(n+1)].next = arr[size-(n-1)]
        return head
        