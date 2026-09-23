class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res, path = [], []

        def dfs(opens, closes):  # counts remaining
            if closes == 0:
                res.append(''.join(path))
                return
            if opens > 0:
                path.append('(')
                dfs(opens - 1, closes)
                path.pop()
            if closes > opens:
                path.append(')')
                dfs(opens, closes - 1)
                path.pop()

        dfs(n, n)
        return res