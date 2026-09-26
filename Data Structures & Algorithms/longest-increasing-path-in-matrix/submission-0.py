class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        memo = {}
        m = len(matrix)
        n = len(matrix[0])

        def dfs(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            
            long = 1
            for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
                if 0<= x+i < m and 0<= y+j< n and matrix[i][j] < matrix[i+x][j+y]:
                    long = max(long,dfs(i+x,y+j)+1)
            memo[(i,j)] = long
            return long


        long = 0
        for i in range(m):
            for j in range(n):
                long = max(long,dfs(i,j))
        
        return long
                
