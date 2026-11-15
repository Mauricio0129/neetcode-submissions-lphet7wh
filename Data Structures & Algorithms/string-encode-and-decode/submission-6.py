class Solution:

    def encode(self, strs: List[str]) -> str:
        content = []
        for string in strs:
            current_lengt = len(string)
            formatted = f"{current_lengt:03d}"
            content.append(f"@{formatted}{string}")
        
        return "".join(content)
        
    def decode(self, s: str) -> List[str]:
        res = []
        global_left = 0
        while global_left < len(s):
            size_current_string = int(s[global_left + 1: global_left + 4])
            start = global_left + 4
            if size_current_string:
                string = s[start: start + size_current_string]
                res.append(string)
            else:
                res.append("")
            global_left = start + size_current_string
        
        return res


