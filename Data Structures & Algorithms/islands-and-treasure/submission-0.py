class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        m = len(grid)
        n = len(grid[0])
        visited = set()
        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((i,j))
        dist = 0
        while q:
            for cell in range(len(q)):
                (i,j) = q.popleft()
                if grid[i][j] == -1 or (i,j) in visited:
                    continue
                visited.add((i,j))
                grid[i][j] = dist
                if i < m-1:
                    q.append((i+1,j))
                if i > 0:
                    q.append((i-1,j))
                if j < n-1:
                    q.append((i,j+1))
                if j > 0:
                    q.append((i,j-1))
            dist += 1
                


            
