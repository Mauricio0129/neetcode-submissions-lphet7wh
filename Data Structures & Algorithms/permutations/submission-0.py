class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return self.helper([], set(), [], nums)

    def helper(self, working_list, look_up, res, nums):
        if len(working_list) == len(nums):
            res.append(working_list.copy())
            return
        
        for i in range(0, len(nums)):
            if nums[i] in look_up:
                continue
            look_up.add(nums[i])
            working_list.append(nums[i])

            self.helper(working_list, look_up, res, nums)

            look_up.remove(nums[i])
            working_list.pop()
        return res


        