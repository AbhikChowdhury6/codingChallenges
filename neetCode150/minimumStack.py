from math import inf
class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_val = inf

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min_val:
            self.min_stack.append([val,1])
            self.min_val = val
        elif val == self.min_val:
            self.min_stack[-1][1] += 1
        print("push")
        print(self.stack)
        print(self.min_stack)


    def pop(self) -> None:
        val = self.stack.pop()
        if val == self.min_stack[-1][0]:
            self.min_stack[-1][1] -= 1
        print("pop")
        print(self.min_stack)
        if self.min_stack[-1][1] == 0:
            self.min_stack.pop()
        if len(self.min_stack) == 0:
            self.min_val = inf

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1][0]
