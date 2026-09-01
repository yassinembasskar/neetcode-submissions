class Solution:
    def isValid(self, s: str) -> bool:
        closing = {"}": "{", ")": "(", "]": "["}
        opening = set(["{", "(", "["])
        pile = []
        for c in s:
            if c in opening:
                pile.append(c)
            elif c in closing:
                if not pile or closing[c] != pile.pop():
                    return False
        return len(pile) == 0