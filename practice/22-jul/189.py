class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = []
        n = len(nums)
        k = k % n

        for i in range(n-k, n):
            res.append(nums[i])

        for i in range(n-k):
            res.append(nums[i])

        for i in range(len(nums)):
            nums[i] = res[i]

