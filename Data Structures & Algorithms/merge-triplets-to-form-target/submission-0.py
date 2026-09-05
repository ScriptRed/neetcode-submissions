class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first = []
        for trip in triplets:
            if trip[0] <= target[0]:
                first.append(trip)
        second = []
        for trip in first:
            if trip[1] <= target[1]:
                second.append(trip)
        third = []
        for trip in second:
            if trip[2] <= target[2]:
                third.append(trip)
        
        f = s = t = False
        for trip in third:
            if trip[0] == target[0]:
                f = True
            if trip[1] == target[1]:
                s = True
            if trip[2] == target[2]:
                t = True
        return f and s and t