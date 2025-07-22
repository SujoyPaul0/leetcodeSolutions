class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        if nums[-1] != len(nums):
            return len(nums)

        for i in range(len(nums)):
            if nums[i] != i:
                return i