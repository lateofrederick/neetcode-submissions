class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack = self.stack[:-1]

    def top(self) -> int:
        if not self.stack:
            return 0
        return self.stack[-1]

    def getMin(self) -> int:
        self.minimum = float('inf')

        for i in self.stack:
            if i < self.minimum:
                self.minimum = i

        return self.minimum
