class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_water_units = 0
        left, right = 0 , len(heights) - 1

        while left < right:
            distance = right - left 
            smallest_wall = min(heights[left], heights[right])
            current_water_units = smallest_wall * distance

            max_water_units = max(max_water_units, current_water_units)

            if heights[left] <= heights[right]:
                left += 1
                continue 
            right -=1
        return max_water_units



