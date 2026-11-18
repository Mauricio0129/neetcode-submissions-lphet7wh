class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_list = [x.lower() for x in s if x.isalnum()]
        clean_string = "".join(clean_list)
        return clean_string == clean_string[::-1]

