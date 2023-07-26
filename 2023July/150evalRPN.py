from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(c))
        return stack[0]
    
if __name__ == "__main__":
    solution = Solution()

    tokens1 = ["2","1","+","3","*"]
    print(solution.evalRPN(tokens1)) # 9

    tokens2 = ["4","13","5","/","+"]
    print(solution.evalRPN(tokens2)) # 6

    tokens3 = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    print(solution.evalRPN(tokens3)) # 22