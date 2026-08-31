# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        self.helper(pairs, 0, len(pairs) - 1)
        return pairs

    def helper(self, pairs, s, e):
        if e - s < 1:
            return 

        pivot = pairs[e]
        insert_pointer = s

        for scan in range(s, e):
            if pairs[scan].key < pivot.key:
                temp = pairs[insert_pointer]
                pairs[insert_pointer] = pairs[scan]
                pairs[scan] = temp
                insert_pointer += 1

        pairs[e] = pairs[insert_pointer]
        pairs[insert_pointer] = pivot

        self.helper(pairs, s, insert_pointer - 1)
        self.helper(pairs, insert_pointer + 1, e)
        

 



