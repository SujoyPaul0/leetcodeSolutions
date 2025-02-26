'''
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
'''
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # Get the number of rows and columns in the matrix
        ROWS, COLS = len(heights), len(heights[0])

        # Sets to track that can flow to the pacific and Atlantic oceans
        pac, atl = set(), set()

        # Depth first search(DFS) function to explore valid paths
        def dfs(r, c, visit, prevHeight):
            # Base case: If the cell is out of bounds, already visited, or cannot be reached
            if (
                (r,c) in visit # already visited
                or r < 0 or c < 0 or r == ROWS or c == COLS # Out of bounds
                or heights[r][c] < prevHeight # Water cannot flow uphill
            ):
                return

            # Mark the current cell as visited
            visit.add((r, c))

            # Explore all four possible directions (down, up, right, left)
            dfs(r + 1, c, visit, heights[r][c]) # Move down
            dfs(r - 1, c, visit, heights[r][c]) # Move up
            dfs(r, c + 1, visit, heights[r][c]) # Move right
            dfs(r, c -1, visit, heights[r][c]) # Move left

        # Start DFS from the pacific ocean (top row and left column)
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c]) # Top row
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c]) # Bottom row

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0]) # Left column
            dfs(r, COLS - 1, atl, heights[r][COLS - 1]) # Right column

        # Collect all cells that can flow to both oceans
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl: # If cell is in both sets
                    res.append([r, c])

        return res