class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return 0
        
        reader = writer = 0
        k = 0

        while reader < len(nums):
            if nums[reader] != val:
                nums[writer] = nums[reader]
                writer += 1
                k += 1
            reader += 1
        return k