class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        count = 0
        intervals.sort()
        print(intervals)
        curr = -50000
        for i,itvl in enumerate(intervals):
            if itvl[0] < curr:
                count += 1
                curr = min(curr,itvl[1])
            else:
                curr = itvl[1]
        
        return count
        

