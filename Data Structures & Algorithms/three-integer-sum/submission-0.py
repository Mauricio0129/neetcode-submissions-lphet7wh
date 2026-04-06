class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        current = 0
        triplets = set()
        while current < len(nums):
            left, right = current + 1, len(nums) -1
            target = nums[current] * -1
            while left < right:
                pair_value = nums[left] + nums[right]
                if pair_value == target:
                    triplets.add((nums[current], nums[left], nums[right]))
                    left +=1 
                    right -=1 
                elif pair_value < target:
                    left += 1
                else:
                    right -=1
            current +=1
        return list(triplets)