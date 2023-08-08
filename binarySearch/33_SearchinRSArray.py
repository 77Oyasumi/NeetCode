from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l+r) // 2
            if target == nums[mid]:
                return mid
            
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                # elif target < nums[l]:
                #     l = mid + 1
                else:
                    r = mid - 1
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                # elif target > nums[r]:
                #     r = mid - 1
                else:
                    l = mid + 1
        return -1
    
if __name__ == "__main__":
    solution = Solution()

    nums1 = [4,5,6,7,0,1,2]
    target1 = 0
    print(solution.search(nums1, target1))

    nums2 = [4,5,6,7,0,1,2]
    target2 = 3
    print(solution.search(nums2, target2))

    nums3 = [6,7,8,9,0,1,2,3,4]
    target3 = 5
    print(solution.search(nums3, target3))

    nums4 = [6,7,8,9,0,1,2,3,4]
    target4 = 6
    print(solution.search(nums4, target4))