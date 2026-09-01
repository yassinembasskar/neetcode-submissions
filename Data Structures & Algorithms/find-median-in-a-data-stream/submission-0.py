class MedianFinder:
    import heapq
    def __init__(self):
        self.top = []
        self.down = []
        self.mid = None

    def addNum(self, num: int) -> None:
        if self.mid is None and not self.top and not self.down:
            self.mid = num
        elif self.mid is not None:
            heapq.heappush(self.top, max(num, self.mid))
            heapq.heappush(self.down, max(-num, -self.mid))
            self.mid = None
        else:
            if num <= self.top[0] and num >= -self.down[0]:
                self.mid = num
            elif num > self.top[0]:
                heapq.heappush(self.top, num)
                self.mid = heapq.heappop(self.top)
            elif num < -self.down[0]:
                heapq.heappush(self.down, -num)
                self.mid = -heapq.heappop(self.down)
            

    def findMedian(self) -> float:
        if self.mid is not None:
            return self.mid
        else: 
            return (self.top[0] - self.down[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()