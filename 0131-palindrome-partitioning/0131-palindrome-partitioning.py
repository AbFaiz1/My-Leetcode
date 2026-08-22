class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        def solve(i, temp):
            if i >= len(s):
                ans.append(temp.copy())
                return
            for j in range(i, len(s)):
                part = s[i:j+1]
                if part == part[::-1]:
                    temp.append(part)
                    solve(j+1, temp)
                    temp.pop()
        solve(0, [])
        return ans