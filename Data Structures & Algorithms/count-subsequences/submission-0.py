class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        #rule: how many ways can we form [:j] using [:i]
        m = len(s) #i
        n = len(t)


        dp = [[0]*(m+1) for _ in range(n + 1)]
        for i in range(len(s)):
            dp[0][i] = 1

        for i in range(1,m+1):
            for j in range(1,n+1):
                if s[i-1] == t[j-1]:
                    dp[j][i] = dp[j-1][i-1] + dp[j][i-1]
                else:
                    dp[j][i] = dp[j][i-1]

        print(dp)

        return dp[-1][-1]
                