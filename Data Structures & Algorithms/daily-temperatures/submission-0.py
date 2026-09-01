class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0]*len(temperatures)
        stack = []
        indexes = {}
        last = -1
        for t in range(len(temperatures)): 
            while stack and temperatures[t] > stack[-1]:
                result[indexes[last]] = t - indexes[last]
                del indexes[last]
                last-=1
                stack.pop()

            stack.append(temperatures[t])
            last +=1
            indexes[last] = t

        return result
