import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # (enqueue, processing, index), sorted descending so pop() gives the earliest
        pending = sorted(((enq, pro, i) for i, (enq, pro) in enumerate(tasks)), reverse=True)
        ready = []   # min-heap of (processing, index)
        res = []
        time = 0

        while pending or ready:
            if not ready and pending[-1][0] > time:
                time = pending[-1][0]          # CPU idle: jump to next arrival

            while pending and pending[-1][0] <= time:
                enq, pro, i = pending.pop()
                heapq.heappush(ready, (pro, i))

            pro, i = heapq.heappop(ready)
            res.append(i)
            time += pro

        return res