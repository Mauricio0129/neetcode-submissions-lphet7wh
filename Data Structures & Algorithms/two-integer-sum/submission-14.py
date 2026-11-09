class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numbers = {}
        for index, val in enumerate(nums):
            if target - val in numbers:
                return[numbers[target - val], index]
            
            numbers[val] = index