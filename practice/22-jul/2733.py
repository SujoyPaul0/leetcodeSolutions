class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return -1

        mini = float('inf')
        maxi = float('-inf')

        for n in nums:
            mini = min(mini, n)
            maxi = max(maxi, n)

        for n in nums:
            if n != mini and n != maxi:
                return n
        return -1