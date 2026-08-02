class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        acc = {}
        res = 0
        for item in nums:
            acc[item] = acc.get(item, 0) + 1
        for item in acc:
            if item - 1 in acc:
                continue
            longcon = 1
            curr = item
            while True:
                if curr + 1 in acc:
                    curr +=1
                    longcon += 1
                else:
                    break
            res = max(longcon,res)
        return res
                