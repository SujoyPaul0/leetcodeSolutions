'''
Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Edge case: If the grid is empty, return 0
        if not grid or not grid[0]:
            return 0

        islands = 0 #  Counter for number of island
        visit = set() # set to keep track of visited cells
        rows, cols = len(grid), len(grid[0]) # Get dimensions of the grid

        # Depth-First Search (DFS) function to explore an island
        def dfs(r, c):
            # Base case: If out of bounds, water cell, or already visited, return
            if (
                r not in range(rows) # index out of bounds
                or c not in range(cols) # Check if column index is out of bounds
                or grid[r][c] == "0" # check if the cell is water ('0')
                or (r, c) in visit # check if the cell is already visited
            ):
                return

            visit.add((r, c)) # Mark the cell as visited
            
            # Defint the four posible movement directions (right, left, down, up)
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

            # Explore all four directions recursively
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        # Iterace over each cell in the grid 
        for r in range(rows):
            for c in range(cols):
                # If a land cell ('1') is found and not visited start DFS
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1 # New island found, increment count
                    dfs(r, c) # Start DFS to mark all connected Land cells

        return islands # return total number of islands