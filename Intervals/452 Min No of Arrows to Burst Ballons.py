'''
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows = len(points)
        prev = points[0]

        for i in range(1, len(points)):
            curr = points[i]

            if curr[0] <= prev[1]:
                arrows -= 1
                prev = [curr[0], min(curr[1], prev[1])]
            else:
                prev = curr
        
        return arrows
        