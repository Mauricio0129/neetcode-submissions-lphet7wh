class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        content = {}
        for c in s:
            content[c] = content.get(c, 0) + 1
        
        for c in t:
            if c not in content:
                return False
            content[c] = content.get(c, 0) - 1
            if  content[c] == 0:
                del content[c]
        
        if not content:
            return True
        return False