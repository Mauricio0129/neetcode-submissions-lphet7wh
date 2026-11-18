class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for first_pick in range(0, len(nums)):
            a = nums[first_pick]
            
            if a > 0:
                break

            if first_pick > 0 and a == nums[first_pick - 1]:
                continue

            left, right = first_pick + 1, len(nums) - 1
    

            while left < right:
                c_number = a + nums[left] + nums[right]

                if (left > first_pick + 1 and nums[left] == nums[left -1]) or c_number < 0 :
                    left += 1
                    continue
                
                elif (right < len(nums) - 1 and nums[right] == nums[right + 1]) or c_number > 0:
                    right -= 1
                    continue

                res.append([a, nums[left], nums[right]])
                left += 1
                right -= 1

        return res
                




            