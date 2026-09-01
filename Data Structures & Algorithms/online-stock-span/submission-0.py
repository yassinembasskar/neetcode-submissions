class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        cumm = 1
        while self.stack:
            if price >= self.stack[-1][0]:
                cumm += self.stack[-1][1]
                self.stack.pop(-1)
            else:
                break   
        self.stack.append((price, cumm))
        return cumm


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)