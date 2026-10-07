class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        return self.helper(0, nums, [], res)

    def helper(self, index, original, current, result):
        if index >= len(original):
            return
        
        for i in range(index, len(original)):
            current.append(original[i])
            result.append(current.copy())
            self.helper(i + 1, original, current, result)
            current.pop()

        return result 


        