class CountSquares:

    def __init__(self):
        self.freq = {}

    def add(self, point: List[int]) -> None:
        if (point[0], point[1]) not in self.freq:
            self.freq[(point[0], point[1])] = 0
        self.freq[(point[0], point[1])] += 1

    def count(self, point: List[int]) -> int:
        res = 0
        for key, val in self.freq.items():
            if key[0] == point[0]:
                d = point[1]-key[1]
                if d == 0:
                    continue
                if (point[0]-d, point[1]) in self.freq and (key[0]-d, key[1]) in self.freq:
                    res += val * self.freq[(point[0]-d, point[1])] * self.freq[(key[0]-d, key[1])]
                if (point[0]+d, point[1]) in self.freq and (key[0]+d, key[1]) in self.freq:
                    res += val * self.freq[(point[0]+d, point[1])] * self.freq[(key[0]+d, key[1])]
        return res 



# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)