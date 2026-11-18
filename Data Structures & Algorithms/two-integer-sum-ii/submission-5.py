class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            current_number = numbers[left] + numbers[right]

            if current_number < target:
                left += 1
                continue

            elif current_number > target:
                right -= 1
                continue
            
            return [left + 1, right + 1]