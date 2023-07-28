from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[int]:
        stack = []
        res = []

        def backTrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append("(")
                backTrack(openN+1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backTrack(openN, closedN+1)
                stack.pop()
            
        backTrack(0,0)
        return res
            
if __name__ == "__main__":
    solution = Solution()

    n = 3
    print(solution.generateParenthesis(n))

    n1 = 2
    print(solution.generateParenthesis(n1))

    n2 = 5
    print(solution.generateParenthesis(n2))