class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        cur_max = cur_min = 1
        res = nums[0]
        for n in nums:
            num = (cur_max*n, cur_min*n, n)
            cur_max, cur_min = max(num), min(num)
            res = max(res, cur_max)

        return res