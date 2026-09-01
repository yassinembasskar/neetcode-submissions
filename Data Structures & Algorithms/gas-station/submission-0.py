class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_tank = 0
        curr_tank = 0
        starting = 0
        for i in range(n):
            diff = gas[i] - cost[i]
            total_tank += diff
            curr_tank += diff
            if curr_tank < 0:
                starting = i + 1
                curr_tank = 0
        return starting if total_tank >= 0 else -1
