class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        tot = 0
        memo = {}

        def bfs(curr):
            if curr == amount:
                return 0 
            
            if curr in memo:
                return memo[curr]

            res = float("inf")
            for coin in coins:
                if curr + coin <= amount:
                    a = bfs(curr + coin)
                    if a == -1:
                        memo[curr+coin] = -1
                        continue
                    res = min(res,1 + a)

            if res == float("inf"):
                return -1
            memo[curr] = res
            return res
        
        return bfs(0)
                

        
