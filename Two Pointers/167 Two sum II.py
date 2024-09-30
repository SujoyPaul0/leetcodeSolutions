'''
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order

Your solution must use only constant extra space.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
Example 2:

Input: numbers = [2,3,4], target = 6
Output: [1,3]
Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
Example 3:

Input: numbers = [-1,0], target = -1
Output: [1,2]
Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
'''

class Solution:
    def twoSum(self, numbers, target: int):
        # create two poiters one pointing at front another at end
        front, end = 0, len(numbers)-1
        while front < end:
          current_sum = numbers[front] + numbers[end]
          if current_sum == target:
            return [front+1, end+1]
          if current_sum < target:
            front += 1
          else: 
            end -= 1
          

