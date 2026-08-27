class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        k = 1
        while k <= (len(b) // len(a)) + 2:  
            s = a * k
            if b in s:
                return k
            k += 1
        return -1