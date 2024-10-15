'''
Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times. 
'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')
        
        while l <= r:
            # If the current subarray is already sorted, return the leftmost element
            if nums[l] <= nums[r]:
                return min(res, nums[l])
            
            # Calculate the middle index
            m = (l + r) // 2
            
            # Update the result to the smallest element found so far
            res = min(res, nums[m])
            
            # If the middle element is greater than or equal to the leftmost element,
            # it means the minimum is in the right half
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                # Otherwise, the minimum is in the left half
                r = m - 1
        
        return res
