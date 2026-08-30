# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        self.helper(pairs, 0, len(pairs) - 1)
        return pairs

    def helper(self, pairs, l, r):
        if r - l <= 0:
            return pairs
        
        m = (r + l) // 2  ## midle

        self.helper(pairs, l, m) ## left

        self.helper(pairs, m + 1, r) ## right 

        self.merge(pairs, l, m, r) ## merge

    def merge(self, pairs, l, m, r):
        stable_copy = pairs.copy()
        stable_pointer = l 

        pointer1 = l
        pointer2 = m + 1

        while pointer1 <= m and pointer2 <= r:
            if stable_copy[pointer1].key <= stable_copy[pointer2].key:
                pairs[stable_pointer] = stable_copy[pointer1]
                pointer1 += 1
            else:
                pairs[stable_pointer] = stable_copy[pointer2]
                pointer2 += 1
            stable_pointer += 1
        
        if pointer1 <= m:
            while pointer1 <= m:
                pairs[stable_pointer] = stable_copy[pointer1]
                pointer1 += 1
                stable_pointer += 1
        else:
            while pointer2 <= r:
                pairs[stable_pointer] = stable_copy[pointer2]
                pointer2 += 1
                stable_pointer += 1
        return 





        

            


    




