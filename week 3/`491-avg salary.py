'''
Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500

'''

class Solution:
    def average(self, salary: List[int]) -> float:
        
        total = 0
        mini = float('inf')
        maxi = float('-inf')
        
        for num in salary:
            if num < mini:
                mini = num 
        
        for num in salary:
            if num > maxi:
                maxi = num
        

        for i in salary:
            total += i
        
        total = total-(mini+maxi)
        avg = total / (len(salary)-2)
        return avg