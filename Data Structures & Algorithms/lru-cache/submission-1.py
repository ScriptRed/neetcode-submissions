class LRUCache:

    def __init__(self, capacity: int):
        self.keyVal = {}
        self.capacity = capacity
        self.count = 0
        self.stack = deque()

    def get(self, key: int) -> int:
        if key in self.keyVal:
            self.stack.remove(key)
            self.stack.append(key)
            return self.keyVal[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.keyVal:
            self.keyVal[key] = value
            self.stack.remove(key)
            self.stack.append(key)
        else:
            if self.count < self.capacity:
                self.count += 1
            else:
                lrs = self.stack.popleft()
                del self.keyVal[lrs]
            self.keyVal[key] = value
            self.stack.append(key)

