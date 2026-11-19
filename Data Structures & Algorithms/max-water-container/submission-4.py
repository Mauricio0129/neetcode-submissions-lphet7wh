class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water_units = 0
        left, right = 0 , len(heights) - 1

        while left < right:
            distance = right - left 
            smallest_wall = min(heights[left], heights[right])
            
            if heights[left] <= heights[right]:
                current_water_units = heights[left] * (right - left)
                left += 1
            else:
                current_water_units = heights[right] * (right - left)
                right -= 1

            max_water_units = max(max_water_units, current_water_units)
        return max_water_units



