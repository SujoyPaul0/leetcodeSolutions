# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        c = head
        while c:
            c = c.next
            count += 1

        dummy = ListNode(0, head)
        left, right = dummy, dummy
        rMove = count-k+1
        while k:      
            k -= 1
            left = left.next

        while rMove:
            rMove -= 1            
            right = right.next
            
        left.val, right.val = right.val, left.val

        return head
        