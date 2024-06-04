class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # x + 2y + 5z = amount
        # dp 紀錄 amount所需的coin_num
        # example dp[11] = min(dp[10]+1, dp[9] + 1, dp[6] + 1)
        def subFunction(amount, cache):
            if amount < 0:
                return math.inf
            elif amount == 0:
                return 0
            elif amount in cache:
                return cache[amount]
            cache[amount] = min(subFunction(amount - c , cache)+1 for c in coins)
            return cache[amount]
        ans = subFunction(amount, {})
        return ans if ans!= math.inf else -1


        