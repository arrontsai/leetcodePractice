class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #用dp解決這個問題，試試看！
        #到i的所有subarray最大的是多少，存在dp裡面
        # initialize..
        dp = []
        dp.append(nums[0])
        maxSum = dp[0]
        for i in range(1,len(nums)):
            dp.append(max(dp[i-1]+nums[i],nums[i]))
            maxSum = max(dp[i],maxSum)
        return maxSum
        