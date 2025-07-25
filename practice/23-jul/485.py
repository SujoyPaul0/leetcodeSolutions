class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        res = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
            else:
                res = max(res, count)
                count = 0

        return max(res, count)    