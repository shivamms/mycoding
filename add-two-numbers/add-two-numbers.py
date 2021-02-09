# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        node1 = l1
        node2 = l2
        l3 = ListNode(0)
        node3 = l3
        bal = 0
        while node1 != None or node2 != None:
            sum = 0
            if node1 != None:
                sum = sum + node1.val
                node1 = node1.next
            if node2 != None:
                sum = sum + node2.val
                node2 = node2.next
            sum = sum + bal
            if sum >= 10:
                bal = 1
                sum = sum - 10
            else:
                bal = 0
            node3.val = sum
            if node1 != None or node2 != None:
                node3.next = ListNode(0)
                node3 = node3.next
        if bal > 0:
            node3.next = ListNode(bal)                
        return l3
        