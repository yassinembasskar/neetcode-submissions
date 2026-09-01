class Solution:
    def isHappy(self, n: int) -> bool:
        res = n
        while res > 9:
            somme = 0
            string = str(res)
            for char in string:
                somme += int(char)**2
            res = somme
        return res == 1 or res == 7