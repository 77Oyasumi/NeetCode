import heapq
from typing import List

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if second > first:
                heapq.heappush(stones, first - second)
            
        stones.append(0)
        
        return abs(stones[0])

if __name__ == "__main__":
    solution = Solution()

    # 測試案例 1
    stones1 = [2, 7, 4, 1, 8, 1]
    print(f"Input: {stones1} -> Output: {solution.lastStoneWeight(stones1)}")  # 預期輸出: 1

    # 測試案例 2
    stones2 = [1, 1]
    print(f"Input: {stones2} -> Output: {solution.lastStoneWeight(stones2)}")  # 預期輸出: 0

    # 測試案例 3
    stones3 = [10]
    print(f"Input: {stones3} -> Output: {solution.lastStoneWeight(stones3)}")  # 預期輸出: 10

    # 測試案例 4
    stones4 = [3, 3, 3]
    print(f"Input: {stones4} -> Output: {solution.lastStoneWeight(stones4)}")  # 預期輸出: 3

    # 測試案例 5
    stones5 = [10, 4, 2, 10]
    print(f"Input: {stones5} -> Output: {solution.lastStoneWeight(stones5)}")  # 預期輸出: 2
