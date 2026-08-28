from functools import lru_cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        @lru_cache(None)
        def solve(i, j, k):
            if k >= len(s3):
                return True
            if i >= len(s1):
                return s2[j:] == s3[k:]
            if j >= len(s2):
                return s1[i:] == s3[k:]
            if s1[i] != s3[k] and s2[j] != s3[k]:
                return False
            if s1[i] == s3[k] and s2[j] == s3[k]:
                c1 = solve(i+1, j, k+1)
                c2 = solve(i, j+1, k+1)
                return c1 or c2
            if s1[i] == s3[k]:
                return solve(i+1, j, k+1)   
            if s2[j] == s3[k]:
                return solve(i, j+1, k+1)         
        return solve(0,0,0)

