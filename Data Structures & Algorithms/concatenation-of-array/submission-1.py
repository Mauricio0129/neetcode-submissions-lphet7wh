class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lenght = len(nums)
        ans = []

        for i in range(lenght * 2):
            ans.append(nums[i % lenght])
            i += 1
        return ans 