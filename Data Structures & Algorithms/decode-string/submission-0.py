class Solution:
    def decodeString(self, s: str) -> str:
        i = 0
        numbers = set(['1', '2', '3', '4', '5', '6', '7' ,'8' , '9', '0'])
        stack = []
        result = ''
        while i < len(s):
            if s[i] in numbers:
                n = ""
                while i < len(s) and s[i] in numbers:
                    n += s[i]
                    i+=1
                stack.append((int(n),len(result)))
            elif s[i] == ']':
                number, place = stack.pop(-1)
                result = result[:place] + number * result[place:]
            elif s[i] != '[':
                result += s[i]
            i+=1
        return result
