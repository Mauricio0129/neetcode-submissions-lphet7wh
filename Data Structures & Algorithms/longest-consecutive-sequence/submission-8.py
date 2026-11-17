class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        
        b_chain_size = 0

        for number in numbers:
            if number - 1 in numbers:
                continue

            c_chain_size = 1
            looking_for = number + 1
            
            while True:
                b_chain_size = max(b_chain_size, c_chain_size)

                if looking_for not in numbers:
                    break

                c_chain_size += 1
                looking_for += 1
                    
        
        return b_chain_size

            
            