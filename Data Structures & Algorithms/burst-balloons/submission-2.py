from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        @cache
        def dfs(l, r):
            if l > r:
                return 0
            maxF = 0
            for i in range(l, r + 1):
                left = nums[l-1] if l > 0 else 1
                right = nums[r+1] if r < len(nums) - 1 else 1
                score = nums[i] * left * right
                maxF = max(maxF, dfs(l, i-1) + score + dfs(i+1, r))
            return maxF
        return dfs(0, len(nums) - 1)