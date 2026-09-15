class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        minim = 1
        maxim = sum(weights)
        cumm = [0] * len(weights)
        for i in range(len(weights)):
            cumm[i] = weights[i]
            if i > 0:
                cumm[i] += cumm[i-1]
        while minim < maxim:
            mid = (minim + maxim) // 2
            i = 0
            j = 0
            counter = 0
            while j < len(cumm):
                if cumm[j] - i < mid:
                    j+=1
                elif cumm[j] - i > mid:
                    if j > 0 and i != cumm[j-1]:
                        i = cumm[j-1]
                        counter+=1
                    else:
                        counter = days+1
                        break
                else:
                    i = cumm[j]
                    counter += 1
                    j+=1
            if i != cumm[-1]:
                counter += 1
            if counter <= days:
                maxim = mid
            else:
                minim = mid + 1
        return minim


