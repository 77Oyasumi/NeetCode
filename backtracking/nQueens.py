from typing import List

class Solution:
    def sloveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        posDiag = set() # (r + c)
        negDiag = set() # (r - c)

        res = []

        board =[["."] * n for i in range(n)]

        def backtracking(r):
            if r == n:
                copy = ["".join(row) for row in board]
                res.append(copy)

            for c in range(n):
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                board[r][c] = "Q"

                backtracking(r + 1)

                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)
                board[r][c] = "."

        backtracking(0)
        return res
    
if __name__ == "__main__":

    sol = Solution()

    n = 4
    print(f"Testing with n = {n}")

    result = sol.sloveNQueens(n)
    print(f"{result}")

    print("Number of solutions:", len(result))
    for idx, solution in enumerate(result, start=1):
        print(f"Solution {idx}:")
        for row in solution:
            print(row)
        print()
