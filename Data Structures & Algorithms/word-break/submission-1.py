class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        memo = {}

        def dfs(sub):
            if sub in memo:
                return memo[sub]
            if not sub:
                return True

            buffer = ""
            for i in range(len(sub)):
                buffer += sub[i]
                if buffer in wordDict:
                    if dfs(sub[i+1:]):
                        memo[sub] = True
                        return True

            memo[sub] = False
            return False

        return dfs(s)