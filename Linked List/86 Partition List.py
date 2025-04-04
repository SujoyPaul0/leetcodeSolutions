'''
Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        lTail, rTail = left, right

        while head:
            if x > head.val:
                lTail.next = head
                lTail = lTail.next
            else:
                rTail.next = head
                rTail = rTail.next
            head = head.next
        
        rTail.next = None
        lTail.next = right.next
        
        return left.next
            