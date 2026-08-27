class Solution:
    def countPalindromes(self, s):
        MOD = 10**9 + 7
        n = len(s)
        leftCount = [0] * 10
        rightCount = [0] * 10
        leftPairs = [[0] * 10 for _ in range(10)]
        rightPairs = [[0] * 10 for _ in range(10)]
        for ch in s:
            rightCount[int(ch)] += 1
        for ch in s:
            x = int(ch)
            rightCount[x] -= 1
            for b in range(10):
                rightPairs[x][b] += rightCount[b]
        rightCount = [0] * 10
        for ch in s:
            rightCount[int(ch)] += 1
        ans = 0
        for i in range(n):
            x = int(s[i])
            rightCount[x] -= 1
            for b in range(10):
                rightPairs[x][b] -= rightCount[b]
            if 2 <= i <= n - 3:
                for a in range(10):
                    for b in range(10):
                        ans += leftPairs[a][b] * rightPairs[b][a]
                ans %= MOD
            for a in range(10):
                leftPairs[a][x] += leftCount[a]

            leftCount[x] += 1
        return ans