class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)

        while l < r:
            mid = (l + r) // 2

            # compute daysNeeded inline
            daysNeeded = 1
            buffer = 0
            for w in weights:
                if buffer + w > mid:
                    daysNeeded += 1
                    buffer = w
                else:
                    buffer += w

            # adjust binary search
            if daysNeeded > days:
                l = mid + 1
            else:
                r = mid

        return l