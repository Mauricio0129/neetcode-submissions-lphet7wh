class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:n] = nums2
            return 
        
        list1_copy = nums1[:m]
        main_pointer = 0
        p1 = 0
        p2 = 0

        while p1 < len(list1_copy) and p2 < len(nums2):
            if list1_copy[p1] <= nums2[p2]:
                nums1[main_pointer] = list1_copy[p1]
                p1 += 1
            else:
                nums1[main_pointer] = nums2[p2]
                p2 += 1
            main_pointer += 1
        
        if p1 < len(list1_copy):
            nums1[main_pointer:] = list1_copy[p1:]
        else:
            nums1[main_pointer:] = nums2[p2:]

