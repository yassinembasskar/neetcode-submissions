class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        mapper = {2: ["a", "b", "c"], 3: ["d", "e", "f"], 4: ["g", "h", "i"],
                    5: ["j", "k", "l"], 6: ["m", "n", "o"], 7: ["p", "q", "r", "s"], 
                    8: ["t", "u", "v"], 9: ["w", "x", "y", "z"]}
        
        res = []
        first_digit = mapper[int(digits[0])]
        next_digits = self.letterCombinations(digits[1:])

        if not next_digits:
            return first_digit

        for first in first_digit:
            for rest in next_digits:
                res.append(first + rest)
                
        return res
            