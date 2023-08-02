from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r :
            m = l + ((r - l) // 2)
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return -1
    
if __name__ == "__main__":

    solution = Solution()

    nums = [-1,0,3,5,9,12]; target = 9
    print(solution.search(nums, target)) # 4

    nums2 = [-1,0,3,5,9,12]; target2 = 2
    print(solution.search(nums2, target2)) # -1
