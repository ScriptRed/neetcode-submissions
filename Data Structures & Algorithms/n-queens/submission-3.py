class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        board = [["."] * n for _ in range(n)]

        cols = set()
        diag = set()       # r - c
        anti = set()       # r + c

        def dfs(r):
            if r == n:
                res.append(["".join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r - c) in diag or (r + c) in anti:
                    continue

                board[r][c] = "Q"
                cols.add(c)
                diag.add(r - c)
                anti.add(r + c)

                dfs(r + 1)

                board[r][c] = "."
                cols.remove(c)
                diag.remove(r - c)
                anti.remove(r + c)

        dfs(0)
        return res
