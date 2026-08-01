class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = [1]*(length)
        suffix = [1]*(length)
        for i in range(1, length, 1):
            prefix[i] = prefix[i-1]*nums[i-1]
            suffix[length - 1 - i] = suffix[length - i] * nums[length - i]
        
        res = []
        for i in range(length):
            res.append(prefix[i]*suffix[i])

        return res



        