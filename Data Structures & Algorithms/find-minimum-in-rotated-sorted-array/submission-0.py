class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while r-l > 1:
            mid = (l + r) // 2
            print(nums[l],nums[mid], nums[r],l,mid,  r)
            if nums[mid] < nums[r] and nums[mid] < nums[l]:
                r = mid
            elif nums[mid] < nums[r] and nums[mid] > nums[l]:
                return nums[l]
            elif nums[mid] > nums[r]:
                l = mid + 1
        return nums[l] if nums[l] < nums[r] else nums[r]