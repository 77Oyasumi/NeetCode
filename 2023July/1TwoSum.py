from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                return[hashmap[diff], i]
            hashmap[n] = i
        return
    
# 创建 Solution 类的实例对象
solution = Solution()

# 测试用例1
nums1 = [2, 7, 11, 15]
target1 = 9
print(solution.twoSum(nums1, target1))

# 测试用例2
nums2 = [3, 5, 8, 11]
target2 = 7
print(solution.twoSum(nums2, target2))

# 测试用例3
nums3 = [2, 3, 4, 5, 6, 7]
target3 = 9
print(solution.twoSum(nums3, target3))

# 测试用例4
nums4 = []
target4 = 9
print(solution.twoSum(nums4, target4))

num5 = [5, 9, 7, 1, 3, 6, 8, 2, 4]
target5 = 11
print(solution.twoSum(num5, target5))

from typing import List

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[List[int]]:
        hashmap = {}
        result = []
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashmap:
                result.append([hashmap[diff], i])
            hashmap[n] = i
        
        return result

solution = Solution2()
num5 = [5, 9, 7, 1, 3, 6, 8, 2, 4]
target5 = 11
print(solution.twoSum(num5, target5))