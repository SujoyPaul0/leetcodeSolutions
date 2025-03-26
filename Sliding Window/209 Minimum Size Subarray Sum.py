'''
Example 1:

Input: target = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: The subarray [4,3] has the minimal length under the problem constraint.
Example 2:

Input: target = 4, nums = [1,4,4]
Output: 1
Example 3:

Input: target = 11, nums = [1,1,1,1,1,1,1,1]
Output: 0
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float("inf")
        
        # iterate as right pointer
        for r in range(len(nums)):
            total += nums[r] # add r th ele to total
            while total >= target:
                res = min(r - l + 1, res)
                total -= nums[l] # substract l the ele from total
                l += 1
        
        return 0 if res == float("inf") else res