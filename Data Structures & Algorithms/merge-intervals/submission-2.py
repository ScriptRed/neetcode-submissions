class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        n = len(intervals)
        i = 0
        intervals.sort()
        while i < n - 1:
            if intervals[i][1] < intervals[i+1][0]:
                res.append(intervals[i])
            else:
                a = min(intervals[i][0],intervals[i+1][0])
                b = max(intervals[i][1],intervals[i+1][1])
                intervals[i+1] = [a,b]
            i += 1
        res.append(intervals[i])
        return res