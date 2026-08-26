class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0
        
        #if you buy a coin, the next is sell or skip
        #if you havent bought a coin, buy or skip.

        #dp = [[0]*n+1 for _ in range(n+1)]

        memo = {}
        def dfs(i,buying):
            if i >= n:
                return 0
            if (i, buying) in memo:
                return memo[i,buying]
            
            
            if buying:
                memo[(i,buying)] = max(dfs(i+1,buying), dfs(i+1,False)- prices[i])
            else:
                memo[(i,buying)] = max(prices[i] + dfs(i+2,True),dfs(i+1,False))
            return memo[(i,buying)]

        return dfs(0, True)

