class Solution:
    def partition(self, s: str) -> List[List[str]]:
        return self.helper(0, [], [], s)

    def helper(self, start, working_list, res, options):
        if start == len(options):
            res.append(working_list.copy())

        for i in range(start, len(options)):
            curr = options[start: i + 1]
            if curr == curr[::-1]:
                working_list.append(curr)
                self.helper(i + 1, working_list, res, options)
                working_list.pop()
            continue
        
        return res 
            


        

