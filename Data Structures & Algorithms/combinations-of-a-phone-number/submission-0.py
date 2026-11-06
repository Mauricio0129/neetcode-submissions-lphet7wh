class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        data_set = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        return self.helper(0, [], [], data_set, digits)


    def helper(self, level, working_list, res, options, digits):
        if level == len(digits):
            res.append("".join(working_list))
            return

        on_use_list = options[digits[level]]
        
        for i in range(0, len(on_use_list)):
            working_list.append(on_use_list[i])
            self.helper(level + 1, working_list, res, options, digits)
            working_list.pop()
        
        return res




