class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        def power(x, y):
            if y == 0:
                return 1
            if y == 1:
                return x
            half = power(x, y//2)
            if y % 2 != 0:
                return x * half * half % MOD
            return half * half % MOD
        word = "".join(map(str, b))
        y = int(word)
        return power(a, y)