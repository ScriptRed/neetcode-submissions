class Solution:
    def solve(self, board: List[List[str]]) -> None:
        ns = set()
        m = len(board)
        n = len(board[0])
        def dfs(i,j):
            directions = [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]
            
            ns.add((i,j))
            
            for x,y in directions:
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'O' and (x,y) not in ns:
                    dfs(x,y)

        for i in range(m):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][n-1] == 'O':
                dfs(i,n-1)
        
        
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0,j)
            if board[m-1][j] == 'O':
                dfs(m-1,j)

        print(ns)

        for i in range(m):
            for j in range(n):
                if (i,j) not in ns:
                    board[i][j] = 'X'