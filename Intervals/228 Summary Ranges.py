'''
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: The ranges are:
[0,2] --> "0->2"
[4,5] --> "4->5"
[7,7] --> "7"
'''
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = []
        start = nums[0]

        for i in range(1,len(nums)):
            if nums[i] != nums[i-1] + 1:
                if start == nums[i-1]:
                    ranges.append(str(start))
                else:
                    ranges.append(str(start) + "->" + str(nums[i-1]))
                start = nums[i]

        # Handle the last range
        if start == nums[-1]:
            ranges.append(str(start))
        else:
            ranges.append(str(start) + "->" + str(nums[-1]))
        
        return ranges