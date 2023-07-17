from typing import List

class Solution:
    def twoSum(self, numbers:List[int], targrt:int) -> List[int]:
        l, r = 0, len(numbers) - 1
        curSum = 0
        
        while l < r :
            curSum = numbers[l] + numbers[r]

            if curSum > targrt:
                r -= 1
            elif curSum < targrt:
                l += 1
            else:
                return [l+1, r+1]
        return []
    
solution = Solution()

numbers1 = [1, 3, 4, 5, 7, 10, 11]
target1 = 9

numbers2 = [-1, 0]
target2 = -1

print(solution.twoSum(numbers1, target1))
print(solution.twoSum(numbers2, target2))