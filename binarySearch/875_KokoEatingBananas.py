from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = max(piles)

        while l <= r:
            k = (l + r) // 2
            hours = 0
            
            for p in piles:
                hours += math.ceil(p / k)
            if hours > h:
                l = k + 1
            else:
                r = k - 1
                res = min(res, k)
        return res

if __name__ == "__main__":

    solution = Solution()

    piles1 = [3,6,7,11]; h1 = 8
    print(solution.minEatingSpeed(piles1, h1)) # 4

    piles2 = [30,11,23,4,20]; h2 = 5
    print(solution.minEatingSpeed(piles2, h2)) # 30

    piles3 = [30,11,23,4,20]; h3 = 6
    print(solution.minEatingSpeed(piles3, h3)) # 23 