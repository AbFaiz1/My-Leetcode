class Solution:
    def countAndSay(self, n: int) -> str:
        s = "1"
        for _ in range(n-1):
            temp = ""
            i = 0
            while i < len(s):
                j = i + 1
                while j < len(s) and s[j] == s[i]:
                    j += 1
                temp += str(j-i) + s[i]
                i = j
            s = temp
        return s
            
