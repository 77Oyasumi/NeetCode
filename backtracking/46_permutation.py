from typing import List

class Solution:
    def permute(self, nums:List[int]) -> List[List[int]]:

        res = []

        if (len(nums) == 1):
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perms = self.permute(nums)

            for perm in perms:
                perm.append(n)
            res.extend(perms)
            nums.append(n)
        return res
    
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    nums1 = [1, 2, 3]
    print("Test Case 1:")
    print("Input:", nums1)
    print("Output:", solution.permute(nums1))

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    print("\nTest Case 2:")
    print("Input:", nums2)
    print("Output:", solution.permute(nums2))

    # Test Case 3
    nums3 = [5, 6, 7]
    print("\nTest Case 3:")
    print("Input:", nums3)
    print("Output:", solution.permute(nums3))

