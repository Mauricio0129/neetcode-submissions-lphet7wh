class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        return self.helper(0, [], [], nums, target)
    
    def helper(self, start_index, curr_combination, res, options, target):
        curr_sum = sum(curr_combination)

        if curr_sum == target:
            res.append(curr_combination.copy())
            return 

        elif curr_sum > target:
            return
        
        for i in range(start_index, len(options)):
            curr_combination.append(options[i])
            self.helper(i, curr_combination, res, options, target)
            curr_combination.pop()

        return res 

        



