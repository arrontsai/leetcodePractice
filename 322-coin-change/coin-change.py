class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # x + 2y + 5z = amount
        # dp 紀錄 amount所需的coin_num
        minCoins = [math.inf for _ in range(amount + 1)]
        minCoins[0] = 0
        # example dp[11] = min(dp[10]+[1, 0, 0], dp[9] + [0, 1, 0], dp[6] + [0, 0, 1])
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    minCoins[i] = min(minCoins[i],minCoins[i-coin]+1)
        if minCoins[amount] == math.inf:
            return -1
        return minCoins[amount]