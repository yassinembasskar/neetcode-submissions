class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        dictionnary = {}
        import heapq
        for ticket in tickets:
            if ticket[0] not in dictionnary:
                dictionnary[ticket[0]] = []
            heapq.heappush(dictionnary[ticket[0]],ticket[1])
        visited = set()
        result = []
        n = len(tickets)
        def dp(st):
            if st not in dictionnary:
                result.append(st)
                return True

            while dictionnary[st]:
                item = heapq.heappop(dictionnary[st])
                dp(item)
            result.append(st)
        
        dp("JFK")
        return result[::-1]