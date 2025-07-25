class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        start = intervals[0]
        res = []

        for i in range(1, len(intervals)):
            if start[1] >= intervals[i][0]:
                if start[1] <= intervals[i][1]:
                    start = [start[0], intervals[i][1]]

            else:
                res.append(start)
                start = intervals[i]
        
        if not res or res[-1] != start:
            res.append(start)

        return res
