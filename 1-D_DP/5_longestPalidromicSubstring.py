class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for i in range(len(s)):
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l : r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1

        return res
    
if __name__ == "__main__":
    solution = Solution()

    # Test case 1: A single character string
    s1 = "a"
    print(solution.longestPalindrome(s1))  # Expected output: "a"

    # Test case 2: Simple palindrome
    s2 = "racecar"
    print(solution.longestPalindrome(s2))  # Expected output: "racecar"

    # Test case 3: String with multiple palindromes
    s3 = "babad"
    print(solution.longestPalindrome(s3))  # Expected output: "bab" or "aba" (either is correct)

    # Test case 4: Even-length palindrome
    s4 = "cbbd"
    print(solution.longestPalindrome(s4))  # Expected output: "bb"

    # Test case 5: No palindrome longer than 1 character
    s5 = "abc"
    print(solution.longestPalindrome(s5))  # Expected output: "a" or "b" or "c" (any single character is correct)

    # Test case 6: All characters are the same
    s6 = "aaaa"
    print(solution.longestPalindrome(s6))  # Expected output: "aaaa"

    # Test case 7: Empty string
    s7 = ""
    print(solution.longestPalindrome(s7))  # Expected output: ""

    # Test case 8: Palindrome at the beginning of the string
    s8 = "abacdfgdcaba"
    print(solution.longestPalindrome(s8))  # Expected output: "aba" or "aca"

    # Test case 9: Palindrome at the end of the string
    s9 = "abb"
    print(solution.longestPalindrome(s9))  # Expected output: "bb"
