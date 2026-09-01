class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        dictionnary = {}
        import heapq
        queue = []
        for h in hand:
            if h not in dictionnary:
                dictionnary[h] = 0
                heapq.heappush(queue, h)
            dictionnary[h] += 1
        while queue:
            item = heapq.heappop(queue)
            if item not in dictionnary:
                continue
            for i in range(groupSize):
                if item + i not in dictionnary:
                    return False
                dictionnary[item+i]-=1
                if dictionnary[item+i] == 0:
                    del dictionnary[item+i]
            if item in dictionnary:
                heapq.heappush(queue, item)
        return True

        

        
