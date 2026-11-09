class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for left in range(len(nums)):
            for right in range(left + 1, len(nums)):
                if nums[left] + nums[right] == target:
                    return [left, right]
        return []