class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if k >= len(nums):
            return len(nums)

        l, r = 0, 0
        zeroCount = 0
        maxWindow = 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zeroCount += 1
            if zeroCount > k:
                maxWindow = max(maxWindow, r - l)
                if nums[l] == 0:
                    zeroCount -= 1
                l += 1
        
        if zeroCount <= k:
            maxWindow = max(maxWindow, r - l + 1)

        return maxWindow
                