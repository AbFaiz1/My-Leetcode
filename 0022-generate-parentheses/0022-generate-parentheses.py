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

            if cb > ob:  # FIX: ob != 0 hatao; ob=0 hone par bhi ')' le sakte hain

                # take: ')' place karo
                solve(i + 1, temp + ")", ob, cb - 1)

                # skip: '(' place karo
                if ob > 0:  
                    solve(i + 1, temp + "(", ob - 1, cb)

            else:
                if ob > 0:  
                    solve(i + 1, temp + "(", ob - 1, cb)

        solve(0, "", n, n)

        return ans