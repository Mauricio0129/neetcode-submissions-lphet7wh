class Solution:
    def isValid(self, s: str) -> bool:
       
        stack = []
        key_map = {"]": "[", "}": "{", ")": "("}

        for c in s:
            if c not in key_map:
                stack.append(c)
            else:
                if not stack:
                    return False
                if key_map[c] != stack[-1]:
                    return False
                stack.pop()
        return not stack