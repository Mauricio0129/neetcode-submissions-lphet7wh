class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        count = 0
        for num in nums:
            if num != 1:
                count = 0
                continue
            print(count)
            count += 1
            max_count = max(count, max_count)
        return max_count