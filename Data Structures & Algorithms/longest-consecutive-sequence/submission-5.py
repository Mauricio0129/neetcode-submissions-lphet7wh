class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        collection = set(nums)
        starts = set()
        longest = 0

        for item in nums:
            if item -1 not in nums:
                starts.add(item)
            
        for item in starts:
            current_lenght = 1
            while item + 1 in collection:
                current_lenght +=1 
                item +=1
            longest = max(longest, current_lenght)
        
        return longest