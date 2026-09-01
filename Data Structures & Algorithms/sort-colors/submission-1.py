class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0,0,0]

        for n in nums:
            counts[n] += 1
            
        insert = 0
        for j in range(len(counts)):
            for _ in range(counts[j]):
                nums[insert] = j
                insert += 1
        
        