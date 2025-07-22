class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hMap = {}
        res = []

        for i, n in enumerate(nums):
            if target - n in hMap:
                res.append([i, hMap[target - n]])
            hMap[n] = i

        return res[0]