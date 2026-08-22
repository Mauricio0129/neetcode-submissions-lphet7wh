# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:

        iterations = []
        if pairs:
            iterations.append(pairs.copy())
        for r in range(1, len(pairs)):
            l = r - 1

            while l >= 0 and pairs[l].key > pairs[l + 1].key:
                temp = pairs[l]
                pairs[l] = pairs[l + 1]
                pairs[l + 1] = temp
                l = l -1
            iterations.append(pairs.copy())
        return iterations


        