'''
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
'''

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        # Iterate through intervals
        for i in range(len(intervals)):
            # Iterate through intervals
            if newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # check for non-overlaps by comparing values
            elif newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # Incase of overlap update newInterval
            else:
                newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
        res.append(newInterval)
        return res