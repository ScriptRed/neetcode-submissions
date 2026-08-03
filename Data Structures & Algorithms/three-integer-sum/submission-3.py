class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        found = []
        for i in range(len(nums) - 2):
            if nums[i-1] == nums[i] and i != 0:
                continue
            j = i+1
            k = len(nums) - 1
            while j < k:
                tot = nums[i] + nums[j] + nums[k]
                if tot == 0:
                    found.append([nums[i],nums[j],nums[k]])
                if tot > 0:
                    while j < k and nums[k-1] == nums[k]:
                        k -= 1
                    k -=1
                else:
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    j +=1
        return found