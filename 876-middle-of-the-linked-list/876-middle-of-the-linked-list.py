# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## using extra space
        # arr = []
        # node = head
        # while node:
        #     arr.append(node)
        #     node = node.next
        # return arr[(len(arr)//2)]
    
        ## two pass without extra space
        # node = head
        # count = 0
        # arr = []
        # while node:
        #     arr.append(node)
        #     count += 1
        #     node = node.next
        # mid = (count // 2) + 1
        # node = head
        # i = 1
        # while i <= mid:
        #     if i == mid:
        #         return node
        #     i += 1
        #     node = node.next
        
        ## Fast and slow pointer
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        