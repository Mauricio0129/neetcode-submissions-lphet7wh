class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        ops = {"+", "D", "C"}

        for op in operations:
            if op in ops:
                if op == "+":
                    r = ans.pop()
                    l = ans.pop()
                    result = l + r
                    ans.extend([l, r, result])
                elif op == "D":
                    r = ans.pop()
                    result = r * 2
                    ans.extend([r, result])
                else:
                    ans.pop()
            else:
                ans.append(int(op))
        return sum(ans)
        