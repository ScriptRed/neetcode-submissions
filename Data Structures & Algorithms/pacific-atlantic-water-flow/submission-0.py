class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        pacific = set()
        atlantic = set()

        def dfs(i, j, visited):
            visited.add((i, j))
            for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= x < m and 0 <= y < n:
                    # Only flow to equal or higher cells
                    if (x, y) not in visited and heights[x][y] >= heights[i][j]:
                        dfs(x, y, visited)

        # Start DFS from Pacific borders
        for i in range(m):
            dfs(i, 0, pacific)
        for j in range(n):
            dfs(0, j, pacific)

        # Start DFS from Atlantic borders
        for i in range(m):
            dfs(i, n-1, atlantic)
        for j in range(n):
            dfs(m-1, j, atlantic)

        # Intersection = cells that can reach both oceans
        return list(pacific & atlantic)
