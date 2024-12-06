from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        maxHeap = [-n for n in nums]

        heapq.heapify(maxHeap)

        count = 0

        while count != k:
            res = heapq.heappop(maxHeap)
            count += 1

        return -res
    
if __name__ == "__main__":
    solution = Solution()
    
    # 測試 1: 一般情況
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    print("測試 1 輸出:", solution.findKthLargest(nums, k))
    # 預期輸出: 5

    # 測試 2: 單一元素
    nums = [1]
    k = 1
    print("測試 2 輸出:", solution.findKthLargest(nums, k))
    # 預期輸出: 1

    # 測試 3: 所有數字相同
    nums = [2, 2, 2, 2, 2]
    k = 3
    print("測試 3 輸出:", solution.findKthLargest(nums, k))
    # 預期輸出: 2

    # 測試 4: 有負數
    nums = [-1, -2, -3, -4, -5]
    k = 1
    print("測試 4 輸出:", solution.findKthLargest(nums, k))
    # 預期輸出: -1

