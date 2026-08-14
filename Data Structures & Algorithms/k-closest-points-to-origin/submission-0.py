class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        distanceToPoint = {}
        for x,y in points:
            distance = math.sqrt((x)**2 + (y)**2)

            heapq.heappush(minheap,(distance, x,y))
        res = []
        for i in range(k):
            d,x,y = heapq.heappop(minheap)
            res.append([x,y])
        return res