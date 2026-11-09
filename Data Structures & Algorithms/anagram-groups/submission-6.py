from collections import defaultdict 
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for word in strs:
            key = [0 for _ in range(0, 26)]
            for char in word:
                key[ord(char) - ord("a")] += 1
            key = tuple(key)
            groups[key].append(word)
        return list(groups.values())