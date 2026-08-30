from functools import cache
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @cache  
        def solve(i, j):
            if j == len(p):
                return i == len(s)
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j + 1 < len(p) and p[j + 1] == "*":
                if solve(i, j + 2):
                    return True
                if match and solve(i + 1, j):
                    return True
            if match:
                if solve(i + 1, j + 1):
                    return True
            return False
        return solve(0, 0)