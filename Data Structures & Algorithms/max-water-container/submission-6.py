class Solution:
    def maxArea(self, heights: list[int]) -> int:
        left, right = 0 , len(heights) -1
        max_water = 0
        
        while left < right:
            smallest = 0
            distance = right - left
            
            if heights[left] > heights[right]:
                smallest = heights[right]
                right -= 1
            else:
                smallest = heights[left]
                left += 1
            
            current = distance * smallest
            
            max_water = max(max_water, current)
        return max_water
         