'''
Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
'''
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        Rows, Cols = len(grid), len(grid[0])

        res = [[float("inf")] * (Cols + 1) for r in range(Rows + 1)]
        res[Rows - 1][Cols] = 0

        for r in range(Rows - 1, -1, -1):
            for c in range(Cols -1, -1, -1):
                res[r][c] = grid[r][c] + min(res[r + 1][c], res[r][c + 1])
        return res[0][0]