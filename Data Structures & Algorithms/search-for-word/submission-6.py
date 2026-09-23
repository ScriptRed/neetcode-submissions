class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        found = []
        visited = set()
        
        def dfs(i,j,pos):
            if pos == len(word):
                #print("here")
                found.append(True)
                return
            visited.add((i,j))
            
            for u,d in [(-1,0),(1,0),(0,1),(0,-1)]:
                #print(f"Looking for {word[pos]} and looking at {i+u} {j+d}")
                if 0 <= i + u < n and 0 <= j + d < m and board[i+u][j+d] == word[pos] and (i+u,j+d) not in visited:
                    #print(board[i+u][j+d],pos)
                    dfs(i+u,j+d,pos+1)
            
            visited.remove((i,j))


        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    dfs(i,j,1)
        

        return any(found)