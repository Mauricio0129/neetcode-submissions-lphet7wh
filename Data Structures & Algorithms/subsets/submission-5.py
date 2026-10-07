class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.helper(0, nums, [], [])

    def helper(self, index, original, current, result):
        if index >= len(original):
            result.append(current.copy())
            return 
        
        for i in range(index, len(original)):
            current.append(original[i])
            self.helper(i + 1, original, current, result)
            current.pop()

        self.helper(i + 1, original, current, result)
        return result 


        