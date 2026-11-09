class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups = {}
        group_number = 0
        for item in strs:
            sorted_version_of_outer_item = "".join(sorted(item))
            if sorted_version_of_outer_item not in groups:
                groups[sorted_version_of_outer_item] = []
                for item2 in strs:
                    sorted_version_of_inner_item = "".join(sorted(item2))
                    if sorted_version_of_inner_item == sorted_version_of_outer_item:
                        groups[sorted_version_of_outer_item].append(item2)
            else:
                continue
        return list(groups.values())