class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre_min = pre_max = glo_max = nums[0]
        for n in nums[1:]:
            cur_min = min(pre_min*n, pre_max*n, n)
            cur_max = max(pre_min*n, pre_max*n, n)
            glo_max = max(glo_max, cur_max)
            pre_min = cur_min
            pre_max = cur_max
        return glo_max