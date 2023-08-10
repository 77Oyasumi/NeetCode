class Solution:
    def length(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res
    
if __name__ == "__main__":
    solution = Solution()

    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"

    print(f"{solution.length(s1)}")
    print(f"{solution.length(s2)}")
    print(f"{solution.length(s3)}")