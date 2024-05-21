class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #要有一個參數存目前最大的值
        #另一個參數去往前加，當變成負的，就再從當下的index開始
        maxSum = curSum = nums[0]
        for i in range(1,len(nums)):
            if curSum >= 0:
                curSum += nums[i]
            else:
                curSum = nums[i]
            maxSum = max(maxSum, curSum)
        return maxSum