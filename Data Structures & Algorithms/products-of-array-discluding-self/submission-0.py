class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        left_product = []
        left = -1
        lenght = len(nums)

        while left < lenght -1:
            if left < 0:
                left_product.append(1)
            else:
                left_product.append(left_product[-1] * nums[left])
            left += 1

        right_product = []
        right = lenght 

        while 0 < right:
            if right == lenght:
                right_product.append(1)
            else:
                right_product.append(right_product[-1] * nums[right])
            right -= 1
        right_product.reverse()

        result = []
        for l , r, in zip(left_product, right_product):
            result.append(l * r)
        return result