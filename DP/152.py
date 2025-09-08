'''
Example 1:
Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1

        for n in nums:
            temp = n * curMax
            curMax = max(n*curMax, n*curMin, n)
            curMin = min(temp, n*curMin, n)
            res = max(curMax, res)

        return res