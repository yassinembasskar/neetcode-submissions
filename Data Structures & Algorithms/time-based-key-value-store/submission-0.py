class TimeMap:

    def __init__(self):
        self.store = {}
        self.timestamps = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.store:
            self.store[key][timestamp] = value
            self.timestamps[key].append(timestamp)
        else:
            self.store[key] = {timestamp: value}
            self.timestamps[key] = [timestamp]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timestamps:
            return ""

        if timestamp in self.store[key]:
            return self.store[key][timestamp]
        
        right = len(self.timestamps[key]) - 1
        left = 0
        while right >= left:
            mid = (right + left) // 2

            if timestamp > self.timestamps[key][mid] and timestamp < self.timestamps[key][right]:
                left = mid
                right -= 1
            elif timestamp < self.timestamps[key][mid]:
                right = mid - 1
            elif timestamp > self.timestamps[key][right]:
                return self.store[key][self.timestamps[key][right]]
            
        return ""
    

        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)