class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hasSet = set(nums)
        res = 0

        for n in hasSet:
            if (n - 1) not in hasSet:
                length = 1
                while (n + length) in hasSet:
                    length += 1
                res = max(length, res)

        return res