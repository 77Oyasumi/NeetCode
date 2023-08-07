from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums)-1

        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        return res
    
if __name__ == "__main__":

    solution = Solution()

    nums1 = [3,4,5,1,2]
    print(solution.findMin(nums1)) # 1

    nums2 = [4,5,6,7,0,1,2]
    print(solution.findMin(nums2)) # 0 

    nums3 = [11,13,15,17]
    print(solution.findMin(nums3)) # 11