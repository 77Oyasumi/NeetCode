from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        nums.sort()

        def backtrack(i, subset):
            if i == len(nums):
                res.append(subset[:])
                return 
            
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop()

            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i + 1, subset)
        backtrack(0, [])
        return res
    
if __name__ == "__main__":
    solution = Solution()
    # Test Case 1
    nums1 = [1, 2, 2]
    print("Test Case 1:")
    print("Input:", nums1)
    print("Output:", solution.subsetsWithDup(nums1))
    
    # Test Case 2
    nums2 = [0]
    print("\nTest Case 2:")
    print("Input:", nums2)
    print("Output:", solution.subsetsWithDup(nums2))
    
    # Test Case 3
    nums3 = [4,4,4,1,4]
    print("\nTest Case 3:")
    print("Input:", nums3)
    print("Output:", solution.subsetsWithDup(nums3))
