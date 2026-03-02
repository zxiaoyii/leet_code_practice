from collections import defaultdict

class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.store[key]
        if not pairs:
            return ""
        lo, hi = 0, len(pairs) - 1
        ans = ""
        while lo <= hi:
            mid = (lo + hi) // 2
            if pairs[mid][0] <= timestamp:
                ans = pairs[mid][1]
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)