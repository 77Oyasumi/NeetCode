from typing import List
from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]

        heapq.heapify(maxHeap)
        
        time = 0
        q = deque()

        while maxHeap or q:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt:
                    q.append([cnt, time + n])
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])
            
        return time
    
if __name__ == "__main__":
    solution = Solution()
    
    # 測資1: 單一任務
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print("Test Case 1:", solution.leastInterval(tasks, n))  # Output: 8

    # 測資2: 冷卻時間為0
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 0
    print("Test Case 2:", solution.leastInterval(tasks, n))  # Output: 6

    # 測資3: 所有任務不同
    tasks = ["A", "B", "C", "D", "E"]
    n = 2
    print("Test Case 3:", solution.leastInterval(tasks, n))  # Output: 5

    # 測資4: 部分冷卻後重複執行
    tasks = ["A", "A", "A", "B", "B", "C", "C"]
    n = 2
    print("Test Case 4:", solution.leastInterval(tasks, n))  # Output: 7

    # 測資5: 單一任務需要多次冷卻
    tasks = ["A", "A", "A", "A"]
    n = 3
    print("Test Case 5:", solution.leastInterval(tasks, n))  # Output: 13

    # 測資6: 只有一個任務
    tasks = ["A"]
    n = 10
    print("Test Case 6:", solution.leastInterval(tasks, n))  # Output: 1

    # 測資7: 空列表
    tasks = []
    n = 5
    print("Test Case 7:", solution.leastInterval(tasks, n))  # Output: 0
