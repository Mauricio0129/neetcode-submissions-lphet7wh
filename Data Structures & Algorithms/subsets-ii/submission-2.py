class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        return self.helper(0, [], [], nums)
        
    
    def helper(self, start, working_space, res, options):
        res.append(working_space.copy())

        for i in range(start, len(options)):

            if i > start and options[i] == options[i - 1]:
                continue
        
            working_space.append(options[i])
            self.helper(i + 1, working_space, res, options)
            working_space.pop()

        return res 



