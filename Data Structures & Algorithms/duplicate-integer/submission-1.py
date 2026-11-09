class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        working_list = []
        for item in nums:
            if item not in working_list:
                working_list.append(item)
            else:
                return True
        return False