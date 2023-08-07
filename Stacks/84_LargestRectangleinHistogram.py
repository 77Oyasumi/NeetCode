from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxarea = 0
        stack = [] # pair (index, height)

        for i, h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                maxarea = max(maxarea, height * (i - index))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxarea = max(maxarea, h * (len(heights) - i))
        return maxarea

if __name__ == "__main__":

    solution = Solution()
    heights1 = [2,1,5,6,2,3]
    print(solution.largestRectangleArea(heights1)) # 10

    heights2 = [2,4]
    print(solution.largestRectangleArea(heights2)) # 4