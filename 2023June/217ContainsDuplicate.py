from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    

# 測試
solution = Solution()

# 測試含有重複數字的列表
print(solution.containsDuplicate([1, 2, 3, 1]))  # True
print(solution.containsDuplicate([4, 5, 6, 7, 8, 9, 7]))  # True
print(solution.containsDuplicate([9, 3, 8, 2, 5, 7, 2]))  # True

# 測試不含重複數字的列表
print(solution.containsDuplicate([1, 2, 3, 4]))  # False
print(solution.containsDuplicate([9, 8, 7, 6, 5]))  # False
print(solution.containsDuplicate([4, 3, 2, 1]))  # False

# 測試空列表
print(solution.containsDuplicate([]))  # False

# 測試只有一個數字的列表
print(solution.containsDuplicate([5]))  # False