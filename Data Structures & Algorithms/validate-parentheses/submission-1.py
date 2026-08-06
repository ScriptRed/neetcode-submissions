class Solution:
    def isValid(self, s: str) -> bool:
        parMap = {
            "(":")",
            "[":"]",
            "{":"}",
        }
        heap = deque()
        for c in s:
            if c in parMap:
                heap.append(parMap[c])
            else:
                if not heap:
                    return False
                if heap.pop() != c:
                    return False
        return len(heap) == 0