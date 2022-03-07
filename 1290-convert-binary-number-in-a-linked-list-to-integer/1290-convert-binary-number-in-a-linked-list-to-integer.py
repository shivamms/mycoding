# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        node = head
        binary = []
        decimalVal = 0
        while node:
            binary.append(node.val)
            node = node.next
        n = len(binary)-1
        for i in range(len(binary)):
            decimalVal += (2**n) * binary[i]
            n -= 1
        return decimalVal