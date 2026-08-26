class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        
        #if you buy a coin, the next is sell or skip
        #if you havent bought a coin, buy or skip.

        #dp = [[0]*n+1 for _ in range(n+1)]

        memo = {}
        def dfs(i):
            if i >= n:
                return 0
            maxf = 0
            for j in range(i+1,n):
                if prices[j]> prices[i]:
                    if j+2 not in memo:
                        memo[j+2] = dfs(j+2)
                    maxf = max(maxf,prices[j]-prices[i] + memo[j+2])

            if i+1 not in memo:
                memo[i+1] = dfs(i+1)
            return max(memo[i+1],maxf)
        
        return dfs(0)




