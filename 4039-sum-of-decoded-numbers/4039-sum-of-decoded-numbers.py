class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        MOD = 10 ** 9 + 7
        ans = 0
        def power(x, y):
            if y == 0:
                return 1
            if y == 1:
                return x
            half = power(x, y//2)
            if y % 2 != 0:
                return x * half * half % MOD
            return half * half % MOD
        for num in nums: 
            width = num % 10
            d = num // 10
            word = str(d)
            base = word[:width]
            base2 = int(base)
            p = word[width:]
            p2 = int(p) % MOD
            ans += power(base2, p2) % MOD
        return ans % MOD


            
