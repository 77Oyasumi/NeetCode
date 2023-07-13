from typing import List

class Solution:
    def longestSeq(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while(n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        return longest
    
solution = Solution()

nums1 = [1, 2, 3, 4, 5]
print(solution.longestSeq(nums1))

nums2 = [100, 4, 200, 1, 3, 2]
print(solution.longestSeq(nums2))

nums3 = [7]
print(solution.longestSeq(nums3))

nums4 = []
print(solution.longestSeq(nums4))

nums5 = [-1, -2, -3, 0, 1, 2, 3]
print(solution.longestSeq(nums5))

nums6 = [1, 2, 2, 3, 3, 3, 4, 5, 5, 5, 5]
print(solution.longestSeq(nums6))
 
nums7 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(solution.longestSeq(nums7))

nums8 = [-3, -2, -1, 0, 1, 2, 3, 4, 5]
print(solution.longestSeq(nums8))

nums9 = [5, 5, 5, 5, 5]
print(solution.longestSeq(nums9))

nums10 = [2, 2, 2, 2, 2, 2]
print(solution.longestSeq(nums10))