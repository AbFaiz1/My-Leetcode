class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        ob = n
        cb = n
        end = n * 2
        def solve(i, temp, ob, cb):
            if i == end:
                ans.append(temp)
                return
            if cb > ob:  
                solve(i + 1, temp + ")", ob, cb - 1)
                if ob > 0:  
                    solve(i + 1, temp + "(", ob - 1, cb)
            else:
                if ob > 0:  
                    solve(i + 1, temp + "(", ob - 1, cb)
        solve(0, "", n, n)
        return ans