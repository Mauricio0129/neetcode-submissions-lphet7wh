class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.helper(0, [], [], nums)
    
    def helper(self, start, curr_nums, res, options):
        res.append(curr_nums.copy())

        for i in range(start, len(options)):
            curr_nums.append(options[i])
            self.helper(i + 1, curr_nums, res, options)
            curr_nums.pop()

        return res
