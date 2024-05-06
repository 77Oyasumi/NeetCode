from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        part = []

        def dfs(i):
            if i >= len(s):
                res.append(part[:])
                return
            for j in range(i, len(s)):
                if self.isPali(s, i, j):
                    part.append(s[i:j + 1])
                    print(f"{part}")
                    dfs(j + 1)
                    part.pop()
                    print(f"{part}")
        dfs(0)
        return res
    
    def isPali(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r - 1
        return True
    
if __name__ == "__main__":

    solution = Solution()
    s = "aab"
    print(f"{solution.partition(s)}")