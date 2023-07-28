class minStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
    
    def pop(self) -> None:
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.stack[-1]
    
    def getmin(self) -> int:
        return self.minStack[-1]
    
if __name__ == "__main__":

    solution = minStack()

    solution.push(5)
    solution.push(3)
    solution.push(7)
    print(solution.getmin())  # 預期輸出: 3
    solution.pop()
    print(solution.getmin())  # 預期輸出: 3
    print(solution.top())     # 預期輸出: 3
    solution.push(10)
    solution.push(2)
    solution.push(6)
    solution.push(1)
    print(solution.getmin())  # 預期輸出: 1
    solution.pop()
    print(solution.getmin())  # 預期輸出: 2
    print(solution.top())     # 預期輸出: 6
    solution.pop()
    print(solution.top())
    print(solution.getmin())
    solution.pop()
    print(solution.top())
    print(solution.getmin())
    solution.pop()
    print(solution.top())
    print(solution.getmin())
    solution.pop()
    print(solution.top())
    print(solution.getmin())