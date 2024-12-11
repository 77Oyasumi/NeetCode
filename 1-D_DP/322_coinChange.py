from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != amount + 1 else -1
    
if __name__ == "__main__":
    solution = Solution()

    coins1 = [1, 5, 10]
    amount1 = 12
    print(f"coins1: {solution.coinChange(coins1, amount1)}")

    coins2 = [2]
    amount2 = 3
    print(f"coins2: {solution.coinChange(coins2, amount2)}")

    coins3 = [1]
    amount3 = 0
    print(f"coins3: {solution.coinChange(coins3, amount3)}")