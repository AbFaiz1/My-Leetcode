class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        def check(i, j):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1: j]
        for i in range(len(s)):
            temp1 = check(i, i)
            temp2 = check(i, i+1)
            if len(temp1) > len(ans):
                ans = temp1
            if len(temp2) > len(ans):
                ans = temp2
            
        return ans

            
