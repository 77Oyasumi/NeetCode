from typing import List

class Solution:
    def climb(self, n: int) -> int:
        one, two = 1, 1

        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one
    
if __name__ == "__main__":

    solution = Solution()
    stair = 1
    print(f"Solution: {solution.climb(stair)}")
    stair = 2
    print(f"Solution: {solution.climb(stair)}")
    stair = 3
    print(f"Solution: {solution.climb(stair)}")
    stair = 4
    print(f"Solution: {solution.climb(stair)}")
    stair = 10
    print(f"Solution: {solution.climb(stair)}")