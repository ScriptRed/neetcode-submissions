class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upper = max(piles)
        lower = 1
        while lower <= upper:
            mid = (lower + upper) // 2
            time = 0
            for item in piles:
                time += math.ceil(item / mid)
            if time > h:
                lower = mid + 1
            else:
                upper = mid - 1
        return lower