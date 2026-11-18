class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        n = len(nums)

        for first_pick in range(n - 2):
            a = nums[first_pick]

            if a > 0:
                break

            if first_pick > 0 and a == nums[first_pick - 1]:
                continue

            left, right = first_pick + 1, n - 1

            while left < right:
                c_number = a + nums[left] + nums[right]

                if c_number < 0:
                    left += 1
                elif c_number > 0:
                    right -= 1
                else:
                    res.append([a, nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

        return res