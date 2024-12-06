from typing import List
import heapq

class Solution:
    def KClosestPoint(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)

        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1

        return res
    
if __name__ == "__main__":
    solution = Solution()
    
    # 測試 1: 基本測試
    points = [[1, 3], [-2, 2], [5, 8], [0, 1]]
    k = 2
    print("測試 1 輸出:", solution.KClosestPoint(points, k))
    # 預期輸出: [[-2, 2], [0, 1]] (順序可能不同)

    # 測試 2: 單一點
    points = [[0, 0]]
    k = 1
    print("測試 2 輸出:", solution.KClosestPoint(points, k))
    # 預期輸出: [[0, 0]]

    # 測試 3: 所有點的距離相同
    points = [[1, 1], [-1, -1], [1, -1], [-1, 1]]
    k = 2
    print("測試 3 輸出:", solution.KClosestPoint(points, k))
    # 預期輸出: [[1, 1], [-1, -1]] (順序可能不同)

    # 測試 5: 負座標值
    points = [[-4, -3], [-2, -2], [1, 1], [3, 3]]
    k = 3
    print("測試 5 輸出:", solution.KClosestPoint(points, k))
    