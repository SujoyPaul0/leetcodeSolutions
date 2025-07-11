class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        visited = set()
        def dfs(r, c):
            if (r >= rows or 
            c >= cols or 
            r < 0 or 
            c < 0 or 
            grid[r][c] == 0 or 
            (r, c) in visited):
                return 0
            else:
                visited.add((r, c))
                return 1 + dfs(r, c + 1) + dfs(r, c - 1) + dfs(r + 1, c) + dfs(r - 1, c)

        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))
        
        return area