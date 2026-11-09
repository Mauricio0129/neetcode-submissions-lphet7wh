class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counterS = {}
        if len(s) != len(t):
            return False
        for c in s:
            counterS[c] = counterS.get(c, 0) + 1
        
        for c in t:
            if c not in counterS:
                return False
            counterS[c] -= 1
            if counterS[c] == 0:
                del counterS[c]
        return True 