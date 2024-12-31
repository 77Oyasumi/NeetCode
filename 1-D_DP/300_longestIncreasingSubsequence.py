from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        LIS = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)
    
if __name__ == "__main__":
    solution = Solution()

    nums = [9,1,4,2,3,3,7]
    print(f"LIS: {solution.lengthOfLIS(nums)}")

    nums = [0,3,1,3,2,3]
    print(f"LIS: {solution.lengthOfLIS(nums)}")