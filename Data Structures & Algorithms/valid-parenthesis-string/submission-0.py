class Solution:
    def checkValidString(self, s: str) -> bool:
        maximum = 0
        minimum = 0
        for char in s:
            if char == "(":
                maximum+=1
                minimum+=1
            if char == ")":
                maximum-=1
                minimum-=1
            if char == "*":
                maximum += 1
                minimum -= 1
            if maximum < 0:
                return False
            if minimum < 0:
                minimum = 0

        return minimum == 0