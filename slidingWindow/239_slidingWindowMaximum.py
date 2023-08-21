import collections
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        q = collections.deque() #index
        l = r = 0

        while r < len(nums):
            # 新來的如果 > q裡面的，裡面的都不要了，直到裡面有一個 > 新來的，或都沒了只剩新來的
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)

            # window 移動，把超出範圍的丟棄
            if l > q[0]:
                q.popleft()

            # if => 看 window 是否擴展到題目要求的k了，達到了，進入條件，把當前 window 內最大的加入結果並縮短左邊窗框
            # 因為迴圈最後 r 也只會推進一步，達到最大之後，永遠都是 l 往前一步 r 才往前一步的狀況而已，不用怕 window 大小超過 k
            if (r + 1) >= k:
                output.append(nums[q[0]])
                l += 1
            r += 1
        return output
    
if __name__ == "__main__":
    solution = Solution()
    nums = [1,3,-1,-3,5,3,6,7]; k = 3
    print(f"{solution.maxSlidingWindow(nums, k)}")