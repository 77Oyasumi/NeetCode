from typing import List

class Solution:
    def trap(self, height:List[int]) -> int:

        l, r = 0, len(height) - 1
        res = 0
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res

solution = Solution()

test1 = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(solution.trap(test1))

test2 = [4,2,0,3,2,5]
print(solution.trap(test2))