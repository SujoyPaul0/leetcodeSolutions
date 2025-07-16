'''
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2
'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        jump, farthest, end = 0, 0, 0

        for i, n in enumerate(nums[:-1]):
            farthest = max(farthest, i + n)

            if i == end:
                end = farthest
                jump += 1
        
        return jump