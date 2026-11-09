class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency_map = {}
        data = [[] for i in range(len(nums) + 1)]

        for item in nums:
            frequency_map[item] = frequency_map.get(item, 0) + 1
        
        for key, item in frequency_map.items():
            data[item].append(key)

        right = len(data) - 1
        result = []

        while len(result) < k:
            if data[right]:
                for item in data[right]:
                    result.append(item)
                    if len(result) == k:
                        break
            right -= 1
        return result