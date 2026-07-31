class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        search = {}
        for i in range(len(nums)):
            if nums[i] in search:
                return [search[nums[i]] , i]
            search[target - nums[i]] = i

        