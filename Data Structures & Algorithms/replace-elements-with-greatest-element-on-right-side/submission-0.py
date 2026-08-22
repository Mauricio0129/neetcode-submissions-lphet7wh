class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        c_max = arr[-1]

        for i in range(len(arr) - 2, -1, -1):
            temp = arr[i]
            arr[i] = c_max
            c_max = max(temp, c_max)

        arr[-1] = -1
        return arr
            