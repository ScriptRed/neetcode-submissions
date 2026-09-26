class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #using the first i nums
        m = sum(nums)
        if target > m:
            return 0
        arr = [0] * (2*m + 1)
        curr = set([m])
        arr[m] = 1

        for num in nums:
            nextarr = [0] * (2*m + 1)
            tempcurr = set()
            for slot in curr:
                nextarr[slot + num] += arr[slot]
                nextarr[slot - num] += arr[slot]
                tempcurr.add(slot + num)
                tempcurr.add(slot - num)
            curr = tempcurr
            arr = nextarr

        return arr[target + m]