from functools import lru_cache
class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10 ** 9 + 7
        @lru_cache(None)
        def solve(temp, dice):
            if dice == n:
                if temp == target:
                    return 1
                return 0
            if temp > target:
                return 0
            ans = 0
            for i in range(1, k+1):
                c1 = solve(temp + i, dice+1)
                ans += c1 % MOD
            return ans % MOD
        return solve(0, 0)

                