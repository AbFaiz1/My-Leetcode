class Solution:
    def countCommas(self, n: int) -> int:
        s = str(n)
        if len(s) <= 3:
            return 0
        return n - 999