class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append((timestamp,value))
        else:
            self.timeMap[key] = [(timestamp,value)]

    def get(self, key: str, timestamp: int) -> str:
        listOf = self.timeMap.get(key, "")
        l = 0
        r = len(listOf) - 1
        res = ""
        while l <= r:
            m = (l + r )// 2
            if listOf[m][0] <= timestamp:
                res = listOf[m][1]
                l = m + 1
            else:
                r = m - 1
        return res

