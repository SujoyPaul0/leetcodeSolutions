# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        p1 = l1
        p2 = l2
        dummy = ListNode(0, None)
        p3 = dummy

        while p2 or p1:
            if p2 and p1:
                sum = p2.val + p1.val + carry
            elif not p2:
                sum = p1.val + carry
            else:
                sum = p2.val + carry
            

            if sum > 9:
                carry = sum // 10
                p3.next = ListNode(sum % 10, None)
                p3 = p3.next 
            else:
                carry = 0
                p3.next = ListNode(sum, None)
                p3 = p3.next

            if p1:
                p1 = p1.next
            if p2:
                p2 = p2.next

        if carry:
            p3.next = ListNode(carry, None)
            
        return dummy.next