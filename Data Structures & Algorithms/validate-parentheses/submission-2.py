class Solution:
    def isValid(self, s: str) -> bool:
        removes = {"]": "[", ")": "(", "}": "{"}

        stack = []

        for char in s:

            if char in removes:
                if not stack:
                    return False

                elif removes[char] != stack[-1]:
                    return False

                stack.pop()

            else:
                stack.append(char)

        return not bool(stack)
