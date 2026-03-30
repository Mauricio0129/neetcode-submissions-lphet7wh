class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_string = ""
        for item in strs:
            encoded_string += f"{len(item)}#{item}#"
        return encoded_string


    def decode(self, s: str) -> list[str]:
        result = []
        index = 0
        while index < len(s):
            stop = []
            while s[index] != "#":
                stop.append(s[index])
                index +=1
            stop = int("".join(stop))
            word = []
            index += 1
            result.append(s[index: index + stop])
            index += stop + 1
        return result 