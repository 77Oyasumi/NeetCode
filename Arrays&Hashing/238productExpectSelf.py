from typing import List

class Solution:
    def productExpectSelf(self, nums:List[int]) -> List[int]:
        res = [1] * (len(nums))

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        
        postfix = 1

        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]
        return res
    
solution = Solution()

arr = [1, 2, 3, 4]

print(solution.productExpectSelf(arr))