from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        
        @cache
        def dfs(left, right):  # exclusive: balloons strictly between left and right
            if right - left < 2:
                return 0
            best = 0
            for k in range(left + 1, right):  # k is last to burst in (left, right)
                best = max(best, nums[left] * nums[k] * nums[right] 
                                + dfs(left, k) + dfs(k, right))
            return best
        
        return dfs(0, n - 1)