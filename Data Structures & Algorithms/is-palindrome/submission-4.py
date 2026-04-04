class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_string = []
        for item in s:
            if item.isalnum():
                clean_string.append(item.lower())
        return clean_string == clean_string[::-1]