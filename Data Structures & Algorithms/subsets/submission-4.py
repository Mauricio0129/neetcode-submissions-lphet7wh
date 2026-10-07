class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        current = []
        return self.helper(0, nums, current, res)

    def helper(self, depth, original, current, result):
        if depth >= len(original):
            result.append(current.copy())
            return result
        
        current.append(original[depth])
        self.helper(depth + 1, original, current, result)

        current.pop()

        self.helper(depth + 1, original, current, result)

        return result 


        