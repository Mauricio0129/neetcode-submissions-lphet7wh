class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        lenght = len(nums)
        ans = []
        j = 0

        for i in range(lenght * 2):
            ans.append(nums[j % lenght])
            j += 1
        return ans 
        

            
