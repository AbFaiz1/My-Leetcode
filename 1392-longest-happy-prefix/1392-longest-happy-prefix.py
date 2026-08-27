class Solution:
    def longestPrefix(self, s: str) -> str:
        left = 0
        right = len(s) - 1
        ans = ""
        best = 0
        while left < len(s)-1:
            s1 = s[:left+1]
            s2 = s[right:]
            if s1 == s2:
                if len(s1) > best:
                    ans = s2
                    best = len(s2)
            left += 1
            right -= 1
        return ans

            
            