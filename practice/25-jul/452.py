class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda pair: pair[0])
        res = []
        start = points[0]

        for i in range(len(points)):
            
            if start[1] >= points[i][0]:
                    start = [start[0], min(points[i][1], start[1])]
            
            else:
                res.append(start)
                start = points[i]

        if not res or res[-1] != start:
            res.append(res)

        return len(res)