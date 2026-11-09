class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        frequency_map = {}
        amount_to_value = {}
        for item in nums:
            frequency_map[item] = frequency_map.get(item, 0) + 1
        
        
        for key, value in frequency_map.items():
            if value not in amount_to_value:
                amount_to_value[value] = [key]
            else:
                amount_to_value[value].append(key)

        content = list(amount_to_value.keys())
        content.sort()
        index = len(content) - 1
        result = []

        while len(result) < k:
            result.extend(amount_to_value[content[index]])
            index -= 1

        return result