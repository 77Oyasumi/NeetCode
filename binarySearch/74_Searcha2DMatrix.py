from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        top, bot = 0, ROWS - 1

        while top <= bot:
            mid = (top + bot) // 2
            if target > matrix[mid][-1]:
                top = mid + 1
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                break
        
        if not (top <= bot):
            return False
        
        mid = (top + bot) // 2
        l ,r = 0, COLS - 1

        while l <= r:
            mid1 = (l + r) // 2
            if target > matrix[mid][mid1]:
                l = mid1 + 1
            elif target < matrix[mid][mid1]:
                r = mid1 - 1
            else:
                return True
        return False
    
if __name__ == "__main__":

    solution = Solution()

    matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]; target1 = 3
    print(solution.searchMatrix(matrix1, target1)) # True

    matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]; target2 = 13
    print(solution.searchMatrix(matrix2, target2)) # False