'''
Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[::])
                return

            # All subsets that include nums[i]
            subset.append(nums[i])
            backtrack(i + 1, subset)
            # pop the recently added ele
            subset.pop()

            # All subset that don't include nums[i] avoid duplicate
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtrack(i + 1, subset)
    
        backtrack(0, [])
        return res
    