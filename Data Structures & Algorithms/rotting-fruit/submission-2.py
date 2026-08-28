class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        rottenFruits = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    rottenFruits.append((i,j))
        if not rottenFruits:
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        return -1
            return 0
        time = -1
        while rottenFruits:
            for i in range(len(rottenFruits)):
                i,j = rottenFruits.popleft()
                if i < m-1 and grid[i+1][j] == 1:
                    rottenFruits.append((i+1,j))
                    grid[i+1][j] = 0
                if i > 0 and grid[i-1][j] == 1:
                    rottenFruits.append((i-1,j))
                    grid[i-1][j] = 0
                if j < n-1 and grid[i][j+1] == 1:
                    rottenFruits.append((i,j+1))
                    grid[i][j+1] = 0
                if j > 0 and grid[i][j-1] == 1:
                    rottenFruits.append((i,j-1))
                    grid[i][j-1] = 0

            time += 1
                    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        
        return time