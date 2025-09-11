'''
Input: nums = [1,2,3,4,5]
Output: [1,2,4,5,3]
Explanation:
When i=1, nums[i] = 2, and the average of its neighbors is (1+4) / 2 = 2.5.
When i=2, nums[i] = 4, and the average of its neighbors is (2+5) / 2 = 3.5.
When i=3, nums[i] = 5, and the average of its neighbors is (4+3) / 2 = 3.5.
'''

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()

        l, r = 0, len(nums)-1

        while len(res) != len(nums):
            res.append(nums[l])
            l += 1

            if l <= r:
                res.append(nums[r])
                r -= 1

        return res