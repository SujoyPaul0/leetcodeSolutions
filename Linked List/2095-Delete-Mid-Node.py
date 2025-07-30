# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l = head
        count = 0
        while l:
            l = l.next
            count += 1

        if count == 1:
            head = None
            return head
        
        mid = count // 2
        res = head

        while mid -1:
            res = res.next
            mid -= 1

        res.next = res.next.next

        return head