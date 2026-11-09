class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}

        for word in strs:
            count = [0] * 26
            for c in word:
                index_to_update = ord(c) - ord("a")
                count[index_to_update] += 1
            key = tuple(count)
            if key not in groups:
                groups[key] = [word]
            else:
                groups[key].append(word)
        return list(groups.values())