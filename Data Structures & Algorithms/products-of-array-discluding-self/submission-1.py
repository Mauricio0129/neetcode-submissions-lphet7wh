class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = [1] * len(nums)

        for i in range(0, len(nums)):
            if not prefix:
                prefix.append(1)
            else:
                prefix.append(prefix[-1] * nums[i - 1])
        
        for i in range(len(nums) - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i + 1]
        
        return [prefix[i] * postfix[i] for i in range(0, len(prefix))]
        
        
            
        
       