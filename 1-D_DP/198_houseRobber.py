from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(n+rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    
if __name__ == "__main__":

    solution = Solution()

    nums = [1,2,3,1]
    print(f"Max money : {solution.rob(nums)}")

    nums2 = [2,7,9,3,1]
    print(f"Max money : {solution.rob(nums2)}")
