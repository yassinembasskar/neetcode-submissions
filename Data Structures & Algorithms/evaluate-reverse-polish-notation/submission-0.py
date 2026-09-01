class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = {"+": lambda x, y: x+y,
                "-": lambda x, y: x-y, 
                "*": lambda x, y: x*y,
                "/": lambda x, y: int(x/y)}
        for t in tokens:
            if t in ops:
                a = stack.pop()
                b = stack.pop()
                stack.append(ops[t](b,a))
            else:
                stack.append(int(t))

        return stack[0]