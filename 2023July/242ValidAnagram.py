class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)

        return Counter(s) == Counter(t)

        if len(s) != len(t):
            return False
        
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get[s[i], 0]
            countT[t[i]] = 1 + countT.get[t[i], 0]
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True
    
solution = Solution()

# 基本測試案例
print(solution.isAnagram("anagram", "nagaram"))  # 預期輸出為 True
print(solution.isAnagram("rat", "car"))  # 預期輸出為 False

# 考慮字母順序不同的情況
print(solution.isAnagram("hello", "olleh"))  # 預期輸出為 True
print(solution.isAnagram("hello", "olelh"))  # 預期輸出為 False

# 考慮不同字母數量的情況
print(solution.isAnagram("aab", "abb"))  # 預期輸出為 False
print(solution.isAnagram("listen", "silent"))  # 預期輸出為 True

# 考慮空字串的情況
print(solution.isAnagram("", ""))  # 預期輸出為 True
print(solution.isAnagram("a", ""))  # 預期輸出為 False

# 考慮大小寫字母的情況
print(solution.isAnagram("Hello", "hello"))  # 預期輸出為 False
print(solution.isAnagram("Hello", "olleH"))  # 預期輸出為 True