'''
Input: nums = [2,3,3,4,6,7], target = 12
Output: 61
Explanation: There are 63 non-empty subsequences, two of them do not satisfy the condition ([6,7], [7]).
Number of valid subsequences (63 - 2 = 61).
'''

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res, mod = 0, (10**9 + 7)
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] + nums[r] > target:
                r -= 1
            else:
                res += 1 << (r - l)
                l += 1

        return res % mod