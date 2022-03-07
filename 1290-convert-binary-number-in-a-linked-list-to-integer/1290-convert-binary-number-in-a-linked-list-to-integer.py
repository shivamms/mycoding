# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # node, binary, decimalVal = head, '', 0
        # while node:
        #     binary += str(node.val)
        #     node = node.next
        # return int(binary,2)
        # n = len(binary)-1
        # for i in range(len(binary)):
        #     decimalVal += (2**n) * binary[i]
        #     n -= 1
        # return decimalVal
        # num = head.val
        # while head.next:
        #     num = num * 2 + head.next.val
        #     head = head.next
        # return num
        ## bit manipulation
        num = head.val
        while head.next:
            num = (num << 1) | head.next.val
            head = head.next
        return num