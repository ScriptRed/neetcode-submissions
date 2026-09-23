class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(curr,level,opens,closes):
            if level < 0:
                return

            if opens == closes == 0:
                res.append(curr)

            if opens > 0:
                dfs(curr + '(',level + 1,opens-1,closes)
            if closes > 0:
                dfs(curr + ')',level - 1,opens,closes - 1)

        dfs('',0,n,n)
        return res