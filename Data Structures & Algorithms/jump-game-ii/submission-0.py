class Solution:
    def jump(self, nums: List[int]) -> int:
        l = 0
        r = 0
        steps = 0
        while r < len(nums)-1:
            maxReach = 0
            while l <= r:
                maxReach = max(maxReach,l + nums[l])
                l += 1
            steps += 1
            l = r+1
            r = maxReach
        return steps
            
