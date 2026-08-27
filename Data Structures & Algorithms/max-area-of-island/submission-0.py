class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0
                
                
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j):
            up = 0
            down = 0
            left = 0
            right = 0
            if grid[i][j] == 1:
                grid[i][j] = 0
                if j>0:
                    up = dfs(i,j-1)
                if j < n-1:
                    down = dfs(i,j+1)
                if i > 0:
                    left = dfs(i-1,j)
                if i<m-1:
                    right = dfs(i+1,j)
            else:
                return 0

            return 1 + up + down + left + right

        for i in range(m):
            for j in range(n):
                if grid[i][j] != 0:
                    found = dfs(i,j)
                    maxArea = max(found, maxArea)
                    
        return maxArea
