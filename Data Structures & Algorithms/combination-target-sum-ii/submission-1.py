class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        curr = []
        size = 0
        res = []
        n = len(candidates)

        def dfs(curr,i,tot):
            if tot < 0:
                return
            if tot == 0:
                res.append(curr.copy())
                return
            if i >= n:
                return

            curr.append(candidates[i])
            dfs(curr,i+1,tot - candidates[i])
            curr.pop()
            while i < n-1 and candidates[i] == candidates[i+1]:
                i += 1
            dfs(curr,i+1,tot)
        
        dfs([],0,target)

        return res
