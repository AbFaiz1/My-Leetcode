from bisect import bisect_left
class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        dp = []
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        for _, h in envelopes:
            if not dp:
                dp.append(h)
            else:
                idx = bisect_left(dp, h)
                if idx == len(dp):
                    dp.append(h)
                else:
                    dp[idx], h = h, dp[idx]
        return len(dp)

