class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        record = dict()
        n = len(nums)
        for i in range(n):
            complement = target - nums[i]
            if complement in record:
                return [record[complement],i]
            record[nums[i]] = i
        return []

        