class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        return self.helper([], 0, 0, [], n * 2)

    def helper(self, working_list, opening, closing, valid_lists, length):
        if len(working_list) == length:
            valid_lists.append("".join(working_list))
            return 
        
        if opening < length // 2:
            working_list.append("(")
            self.helper(working_list, opening + 1, closing, valid_lists, length)
            working_list.pop()
        
        if closing < opening:
            working_list.append(")")
            self.helper(working_list, opening, closing + 1, valid_lists, length)
            working_list.pop()
        
        return valid_lists

        