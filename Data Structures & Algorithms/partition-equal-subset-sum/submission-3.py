class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 == 1:
            return False
        target /= 2
        dp = set([nums[0],0])
        for i in range(1,len(nums)):
            next_dp = set()
            for item in dp:
                new = item + nums[i]
                if new == target:
                    return True
                if new < target:
                    next_dp.add(new)
            dp |= next_dp
        return False


