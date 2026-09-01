class MinStack:

    def __init__(self):
        self.minimums = []
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.minimums or self.minimums[-1] >= val:
            self.minimums.append(val)

            

    def pop(self) -> None:
        if self.stack:
            popped = self.stack.pop()
            if self.minimums[-1] == popped:
                self.minimums.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

    def getMin(self) -> int:
        if self.minimums:
            return self.minimums[-1]
