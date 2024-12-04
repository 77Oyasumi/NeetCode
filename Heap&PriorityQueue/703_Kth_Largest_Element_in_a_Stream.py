import heapq
from typing import List

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0]
    
if __name__ == "__main__":
    # 初始化 KthLargest，設 k = 3，nums = [4, 5, 8, 2]
    kthLargest = KthLargest(3, [4, 5, 8, 2])

    # 添加新數字並打印第 k 大的元素
    print(kthLargest.add(3))  # 添加 3，返回第 3 大的數，應該是 4
    print(kthLargest.add(5))  # 添加 5，返回第 3 大的數，應該是 5
    print(kthLargest.add(10)) # 添加 10，返回第 3 大的數，應該是 5
    print(kthLargest.add(9))  # 添加 9，返回第 3 大的數，應該是 8
    print(kthLargest.add(4))  # 添加 4，返回第 3 大的數，應該是 8
    
