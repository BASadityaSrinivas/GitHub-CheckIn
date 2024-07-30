class TimeMap:

    def __init__(self):
        self.store = {}      

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key].append([value, timestamp])
        else:
            self.store[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            for i in range(len(self.store[key])-1, -1, -1):
                v, ts = self.store[key][i]
                if ts <= timestamp:
                    return v
            return ""
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)