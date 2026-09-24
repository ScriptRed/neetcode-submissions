class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return [["Q"]]

        grid = [['.'] * n for _ in range(n)]
        validGrids = []

        def checkqueen(i, j):
            for a in range(n):
                if grid[a][j] == 'Q':
                    return False
                if grid[i][a] == 'Q':
                    return False

            a, b = i, j
            while a > 0 and b > 0:
                a -= 1
                b -= 1
                if grid[a][b] == 'Q':
                    return False

            a, b = i, j
            while a > 0 and b < n - 1:
                a -= 1
                b += 1
                if grid[a][b] == 'Q':
                    return False

            a, b = i, j
            while a < n - 1 and b > 0:
                a += 1
                b -= 1
                if grid[a][b] == 'Q':
                    return False

            a, b = i, j
            while a < n - 1 and b < n - 1:
                a += 1
                b += 1
                if grid[a][b] == 'Q':
                    return False

            return True

        def dfs(row):
            if row == n:
                validGrids.append(["".join(r) for r in grid])
                return

            for col in range(n):
                if checkqueen(row, col):
                    grid[row][col] = 'Q'
                    dfs(row + 1)
                    grid[row][col] = '.'

        dfs(0)
        return validGrids
