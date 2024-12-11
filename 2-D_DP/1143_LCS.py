class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for j in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        

        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1,):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])
        return dp[0][0]
    
if __name__ == "__main__":
    solution = Solution()

    text1 = 'cat'
    text2 = 'crabt'
    print(f"ans1: {solution.longestCommonSubsequence(text1, text2)}")

    text3 = "abcd"
    text4 = "abcd"
    print(f"ans2: {solution.longestCommonSubsequence(text3, text4)}")

    text5 = "abcd"
    text6 = "efgh"
    print(f"ans2: {solution.longestCommonSubsequence(text5, text6)}")