from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtrack(cur, pos, total):

            if total == target:
                res.append(cur[:])
                return
            
            if total > target:
                return

            prev = -1

            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, total + candidates[i])
                cur.pop()
                prev = candidates[i]
        
        backtrack([], 0, 0)
        return res
    
if __name__ =="__main__":
    solution = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    total = 8
    print(solution.combinationSum2(candidates, total))