# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        left = node
        right = node
        
        while left.next:
            left.val = left.next.val
            left = left.next
            if left.next:
                right = right.next

        right.next = None

        
            