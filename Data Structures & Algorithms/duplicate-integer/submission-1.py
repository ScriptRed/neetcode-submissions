class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for item in nums:
            if item in seen:
                return True
            else:
                seen[item] = 1
        return False
        
        #BEST IS: return len(set(nums)) < len(nums)