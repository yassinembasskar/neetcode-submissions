class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("+inf")
        gap = 0
        start = 0
        while start < len(prices):
            if prices[start] < min_price:
                min_price = prices[start]
            elif prices[start] > min_price:
                if prices[start] - min_price > gap:
                    gap = prices[start] - min_price
            start+=1
                 
        return gap