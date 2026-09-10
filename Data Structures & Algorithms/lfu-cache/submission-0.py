class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dictionnary = {} 
        self.freq_to_keys = defaultdict(OrderedDict)
        self.min_freq = 0
        self.counter = 0
    
    def _bump(self, key: int, freq: int):
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        self.freq_to_keys[freq+1][key] = None

    def get(self, key: int) -> int:
        if key not in self.dictionnary:
            return -1
        freq, usage, val = self.dictionnary[key]
        self._bump(key, freq)
        self.dictionnary[key] = (freq+1, self.counter, val)
        self.counter+=1
        
        return val


    def put(self, key: int, value: int) -> None:
        if key in self.dictionnary:
            freq, _, _ = self.dictionnary[key]
            self._bump(key, freq)
            self.dictionnary[key] = (freq+1, self.counter, value)

        else:
            if len(self.dictionnary) == self.capacity:
                evict_key, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
                del self.dictionnary[evict_key]
            self.dictionnary[key] = (0, self.counter, value)
            self.freq_to_keys[0][key] = None
            self.min_freq = 0

        self.counter+=1
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)