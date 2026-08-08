class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        islands = 0

        def dfs(i, j):
            # Outside grid or water
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return

            # Mark land as visited
            grid[i][j] = '0'

            # Visit all 4 directions
            dfs(i + 1, j)  # Down
            dfs(i - 1, j)  # Up
            dfs(i, j + 1)  # Right
            dfs(i, j - 1)  # Left

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    dfs(i, j)

        return islands