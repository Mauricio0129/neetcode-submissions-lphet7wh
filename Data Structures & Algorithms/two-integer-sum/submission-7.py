class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        right = 0
        while right < len(nums):
            looking_for = target - nums[right]
            if looking_for in seen:
                return [seen[looking_for], right]
            seen[nums[right]] = right
            right += 1