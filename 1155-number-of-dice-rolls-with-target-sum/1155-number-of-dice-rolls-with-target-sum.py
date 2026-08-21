class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        mp = {}
        def solve(temp, dice):
            if temp > target:
                return 0
            if temp == target:
                if dice  == n:
                    return 1
                return 0
            if dice >= n:
                return 0
            if (temp, dice) in mp:
                return mp[(temp, dice)]
            ans = 0
            for i in range(1, k+1):
                choice = solve(temp + i, dice + 1)
                ans += choice
            mp[(temp, dice)] = ans %(10**9 + 7)
            return mp[(temp, dice)]
        return solve(0, 0) % (10**9 + 7)
                