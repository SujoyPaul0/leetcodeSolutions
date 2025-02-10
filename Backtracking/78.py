'''
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
Example 2:

Input: nums = [0]
Output: [[],[0]]
'''

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        subset = []
        def dfs(i):
            # if i is out of bound
            if i >= len(nums):
                # append subset to res
                res.append(subset.copy())
                return

            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)  

            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)
            

        dfs(0)
        return res