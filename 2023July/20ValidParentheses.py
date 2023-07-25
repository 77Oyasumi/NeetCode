class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        closeToOpen = {")":"(", "]":"[", "}":"{"}

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
    
if __name__ == "__main__":

    solution = Solution()

    str1 = "()"
    print(solution.isValid(str1))

    str2 = "()[]{}"
    print(solution.isValid(str2))

    str3 = "(]"
    print(solution.isValid(str3))