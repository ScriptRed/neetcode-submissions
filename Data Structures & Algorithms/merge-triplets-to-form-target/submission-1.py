class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first = []
        for trip in triplets:
            if trip[0] <= target[0] and trip[1] <= target[1] and trip[2] <= target[2]:
                first.append(trip)

        
        f = s = t = False
        for trip in first:
            if trip[0] == target[0]:
                f = True
            if trip[1] == target[1]:
                s = True
            if trip[2] == target[2]:
                t = True
        return f and s and t