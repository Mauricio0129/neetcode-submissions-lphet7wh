class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        content = {}
        for i in range(len(nums)):
            looking_for = target - nums[i]
            if looking_for in content:
                return [content[looking_for], i] 
            content[nums[i]] = i