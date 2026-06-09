class MinStack:

    def __init__(self):
        self.stack = []
        self.extraStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.extraStack:
            self.extraStack.append(min(val, self.extraStack[-1]))
        else:
            self.extraStack.append(val)


    def pop(self) -> None:
        self.stack.pop()
        self.extraStack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.extraStack[-1]


        
