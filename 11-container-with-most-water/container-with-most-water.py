class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 用左右兩邊比較，較短的一個一邊持續往前移
        max_area = cur_area = 0
        left = 0
        right = len(height) - 1
        while left < right:
            cur_area = (right - left) * min(height[left],height[right])
            max_area = max(cur_area,max_area) 
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area
