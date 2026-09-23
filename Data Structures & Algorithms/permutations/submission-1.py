class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        boolarr = [False]*len(nums)

        def dfs(curr):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for j in range(len(nums)):
                if not boolarr[j]:
                    curr.append(nums[j])
                    boolarr[j] = True
                    dfs(curr)
                    curr.pop()
                    boolarr[j] = False



        for i in range(len(nums)):
            boolarr[i] = True
            dfs([nums[i]])
            boolarr[i] = False

        return(res)