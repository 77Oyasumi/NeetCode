'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum():
                newStr += c.lower()
        return newStr == newStr[::-1]
'''

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while r > l and not self.alphanum(s[r]):
                r -= 1
            if (s[l].lower() != s[r].lower()):
                return False
            r -= 1
            l += 1
        return True
            
    def alphanum(self, c):
        return(ord('A') <= ord(c) <= ord('Z') 
               or ord('a') <= ord(c) <= ord('z') 
               or ord('0') <= ord(c) <= ord('9'))
    
solution = Solution()

s1 = "level"
print(solution.isPalindrome(s1))

s2 = "hello"
print(solution.isPalindrome(s2))

s3 = "A man, a plan, a canal: Panama"
print(solution.isPalindrome(s3))

s4 = ""
print(solution.isPalindrome(s4))

s5 = "   "
print(solution.isPalindrome(s5))