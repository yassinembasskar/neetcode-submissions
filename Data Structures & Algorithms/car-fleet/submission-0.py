class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) < 2:
            return len(position)
        
        couples = []
        for i in range(len(position)):
            couples.append((position[i], speed[i]))
        couples = sorted(couples, reverse=True)
        fleet = 0
        time = []

        for c in couples:
            x = (target - c[0]) / c[1]
            if not time:
                time.append(x)
                continue
            if time[-1] < x:
                time.append(x)
                
        return len(time)

