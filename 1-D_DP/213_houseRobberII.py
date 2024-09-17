from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        
    def helper(self, nums):
        r1, r2 = 0, 0

        for n in nums:
            temp = max(r1 + n, r2)
            r1 = r2
            r2 = temp
        return r2

if __name__ == "__main__":
    solution = Solution()

    # Test case 1: Basic case with only one house
    nums1 = [5]
    print(solution.rob(nums1))  # Expected output: 5

    # Test case 2: Houses in a linear sequence
    nums2 = [2, 3, 2]
    print(solution.rob(nums2))  # Expected output: 3 (rob house 2)

    # Test case 3: Alternating high values
    nums3 = [1, 2, 3, 1]
    print(solution.rob(nums3))  # Expected output: 4 (rob house 1 and 3)

    # Test case 4: All values are equal
    nums4 = [4, 4, 4, 4]
    print(solution.rob(nums4))  # Expected output: 8 (rob house 1 and 3 or house 2 and 4)

    # Test case 5: Large number of houses
    nums5 = [6, 7, 1, 30, 8, 2, 4]
    print(solution.rob(nums5))  # Expected output: 41 (rob house 2, 4, and 7)
