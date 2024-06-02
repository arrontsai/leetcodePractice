class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # 先創一個dp 會跟 nums一樣長，default = 1 
        # 每個dp[i] 代表 第ith位置最長的subsequence長度
        # 如果要求 dp[i] 是多少 就等於 max(dp[i], dp[i-1] + 1)
        n = len(nums)
        dp = [1] * n
        for i in range(1,n):
            for j in range(0,i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i],dp[j] + 1)


        return max(dp)
