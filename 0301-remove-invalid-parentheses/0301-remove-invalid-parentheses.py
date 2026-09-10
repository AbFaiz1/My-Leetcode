class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        ans = []
        memo = set()                        

        def check(s):
            count = 0
            for ch in s:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        def solve(i, s):
            if (i, s) in memo:            
                return
            memo.add((i, s))                

            if i >= len(s):
                if check(s):
                    ans.append(s)
                return

            solve(i+1, s)

            new = s[0:i] + s[i+1:]
            solve(i, new)

        solve(0, s)

        ans = list(set(ans))

        count = 0
        ans2 = []

        for each in ans:
            count = max(count, len(each))

        for w in ans:
            if len(w) == count:
                ans2.append(w)

        return ans2