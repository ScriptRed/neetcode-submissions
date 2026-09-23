class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def dfs(curr, i):
            res.append(curr.copy())
            for j in range(i, len(nums)):
                # skip duplicates at the SAME depth
                if j > i and nums[j] == nums[j - 1]:
                    continue
                curr.append(nums[j])
                dfs(curr, j + 1)
                curr.pop()

        dfs([], 0)
        return res