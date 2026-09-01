class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        result = []
        for n in nums:
            if n in frequencies:
                frequencies[n] += 1
            else:
                frequencies[n] = 1

        res = {cle: v for cle, v in sorted(frequencies.items(), key = lambda item: item[1], reverse=True)}
        for cle, v in res.items():
            if k == 0:
                return result
            result.append(cle)
            k-=1
        return result 