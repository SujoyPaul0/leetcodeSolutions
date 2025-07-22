class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        hMap = {0:0, 1:0, 2:0}
        res = []

        for n in nums:
            hMap[n] += 1

        for key, value in hMap.items():
            for i in range(value):
                res.append(key)

        for i in range(len(nums)):
            nums[i] = res[i]