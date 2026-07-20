class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for i in range(len(operations)):
            if operations[i] == '+':
                ans.append(ans[-1] + ans[-2])
            elif operations[i] == 'C':
                ans.pop()
            elif operations[i] == 'D':
                ans.append(2 * ans[-1])
            else:
                ans.append(int(operations[i]))
        res = 0
        for n in ans:
            res += n
        return res
