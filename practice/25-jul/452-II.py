class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        prev = points[0]
        arrow = len(points)

        for i in range(1, len(points)):
            cur = points[i]

            if cur[0] <= prev[1]:
                arrow -= 1
                prev = [prev[0], min(cur[1], prev[1])]

            else:
                prev = cur

        return arrow
