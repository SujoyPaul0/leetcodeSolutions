'''
A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.

Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

 

Example 1:

Input: arr = [3,5,1]
Output: true
Explanation: We can reorder the elements as [1,3,5] or [5,3,1] with differences 2 and -2 respectively, between each consecutive elements.
Example 2:

Input: arr = [1,2,4]
Output: false
Explanation: There is no way to reorder the elements to obtain an arithmetic progression.
'''

class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()  # Sort the array in place
        
        x = len(arr)
        
        for i in range(x - 1):
            if arr[i+1] - arr[i] != arr[1] - arr[0]:
                return False  # Return False as soon as a mismatch is found
        
        return True  # Return True if all differences are consistent
