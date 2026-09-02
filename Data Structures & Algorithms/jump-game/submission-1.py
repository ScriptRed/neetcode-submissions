class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = 0
        maxG = 0
        while i < len(nums) and i <= maxG:
            maxG = max(maxG,nums[i]+i)
            i += 1

        return maxG >= len(nums)-1
