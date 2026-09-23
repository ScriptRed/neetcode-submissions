class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def dfs(sub,i,j):
            if j == len(s):
                if i< j and s[i:j] == (s[i:j])[::-1]:
                    sub.append(s[i:j])
                    res.append(sub.copy())
                    sub.pop()
                return
            
            if i< j-1 and s[i:j] == (s[i:j])[::-1]:
                sub.append(s[i:j])
                dfs(sub,j,j)
                sub.pop()

            dfs(sub,i,j+1)
            
            if i == j:
                sub.append(s[i])
                dfs(sub,i+1,j+1)
                sub.pop()

            
        dfs([],0,0)

        return res
