class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return self.helper(0, [], [], nums)

    def helper(self, start, current, res, options):
        res.append(current.copy())

        for i in range(start, len(options)):
            current.append(options[i])
            self.helper(i + 1, current, res, options)
            current.pop()
        return res