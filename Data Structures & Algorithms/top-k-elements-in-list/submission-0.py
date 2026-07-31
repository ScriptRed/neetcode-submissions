class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = {}
        for item in nums:
            if item not in res:
                res[item] = 1
            else:
                res[item] += 1
        result = []
        for i in range(k):
            mf = max(res.values())
            for key,item in res.items():
                if item == mf:
                    result.append(key)
                    res[key] = 0
                    break

        return result
            
        