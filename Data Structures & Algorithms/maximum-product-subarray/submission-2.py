class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        minPro = 1
        maxPro = 1

        for i in range(0,len(nums)):
            prev = maxPro * nums[i]
            maxPro = max(nums[i],nums[i]*maxPro,nums[i]*minPro)
            minPro = min(nums[i],prev,nums[i]*minPro)
            res = max(res,maxPro)

        return res
