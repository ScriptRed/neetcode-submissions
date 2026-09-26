class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #using the first i nums
        m = sum(nums)
        if target > m:
            return 0
        arr = [0] * (2*m + 1)
        curr = set([nums[0]+m,-nums[0]+m])
        arr[nums[0]+m] += 1
        arr[-nums[0]+m] += 1

        for i in range(1,len(nums)):
            nextarr = [0] * (2*m + 1)
            tempcurr = set()
            for slot in curr:
                nextarr[slot + nums[i]] += arr[slot]
                nextarr[slot - nums[i]] += arr[slot]
                tempcurr.add(slot + nums[i])
                tempcurr.add(slot - nums[i])
            curr = tempcurr
            arr = nextarr

        return arr[target + m]