class Solution:
    def countSubstrings(self, s: str) -> int:
        def expand(i, j, count):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
                count += 1
            return count
        ans = 0
        for i in range(len(s)):
            c1 = expand(i, i, 0)
            c2 = expand(i, i+1, 0)
            ans += c1 + c2
        return ans
            