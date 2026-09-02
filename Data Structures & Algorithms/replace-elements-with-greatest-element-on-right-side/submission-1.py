class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        biggest_seen = -1

        for i in range(len(arr) -1, -1, -1):
            temp = arr[i]
            arr[i] = biggest_seen
            biggest_seen = max(biggest_seen, temp)
        return arr
