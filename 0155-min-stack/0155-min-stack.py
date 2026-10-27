class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, value: int) -> None:
        lastElement = len(self.stack) - 1
        if lastElement < 0:
            self.stack.append((value, value)) # value is the minimum since it is the only element in list
        elif value < self.stack[lastElement][1]:
            self.stack.append((value, value)) # value is minimum since it is the smallest element
        else:
            priorMin = self.stack[lastElement][1]
            self.stack.append((value, priorMin))

    def pop(self) -> None:
        element = self.stack.pop()

    def top(self) -> int:
        topElement = len(self.stack) -1
        return self.stack[topElement][0]
        

    def getMin(self) -> int:
        lastElement = len(self.stack) - 1
        return self.stack[lastElement][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()