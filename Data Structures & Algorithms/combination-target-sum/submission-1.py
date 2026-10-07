class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        return self.helper(0, [], res, nums, target)

    def helper(self, start_i, curr, res, original, target):
        current_sum = sum(curr)

        if current_sum == target:
            res.append(curr.copy())
            return res
        
        elif current_sum > target:
            return res

        for i in range(start_i, len(original)):
            curr.append(original[i])
            self.helper(i, curr, res, original, target)
            curr.pop()

        return res

        

