'''
Input: n = 2, k = 1
Output: 0
Explanation: 
row 1: 0
row 2: 01
'''

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        cur = 0
        left, right = 0, 2**(n-1)
        for _ in range(n-1):
            mid = (left + right) // 2
            if k <= mid:
                right = mid
            else:
                left = mid + 1
                cur = 0 if cur else 1
            
        return cur