class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = []
        for item in s:
            if item.isalnum():
                clean_string.append(item.lower())
        clean_string = "".join(clean_string)
        return clean_string == clean_string[len(clean_string)-1::-1]