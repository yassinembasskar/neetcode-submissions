import heapq
class FreqStack:

    def __init__(self):
        self.frequencies = {}
        self.queue = [] 
        self.stack = []
        self.index = 0

    def push(self, val: int) -> None:
        if val not in self.frequencies:
            self.frequencies[val] = 0
        self.frequencies[val] += 1
        freq = self.frequencies[val]
        ind = self.index
        heapq.heappush(self.queue, (-freq, -ind, val))
        self.index += 1

    def pop(self) -> int:
        freq, _, val = heapq.heappop(self.queue)
        self.frequencies[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()