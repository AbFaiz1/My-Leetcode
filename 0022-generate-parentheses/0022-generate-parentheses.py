class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        k = 2*n
        ans = []
        def solve(i, ob, cb, temp):
            if i >= k:
                ans.append("".join(temp))
                return
            if cb > ob:
                temp.append(')')
                solve(i+1, ob, cb-1, temp)
                temp.pop()
            if ob > 0:
                temp.append('(')
                solve(i+1, ob-1, cb, temp)
                temp.pop()
        solve(0, n, n, [])
        return ans
