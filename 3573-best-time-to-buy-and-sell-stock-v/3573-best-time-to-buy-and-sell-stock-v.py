class Solution:
    def maximumProfit(self, prices, k):
        NEG = float('-inf')

        # dp[t][state]
        # state 0 = FLAT
        # state 1 = LONG
        # state 2 = SHORT
        dp = [[NEG] * 3 for _ in range(k + 1)]

        dp[0][0] = 0

        for price in prices:

            # Copy previous day's states
            new = [row[:] for row in dp]

            for t in range(k + 1):

                # FLAT -> LONG : BUY
                new[t][1] = max(
                    new[t][1],
                    dp[t][0] - price
                )

                # FLAT -> SHORT : SELL
                new[t][2] = max(
                    new[t][2],
                    dp[t][0] + price
                )

                if t < k:

                    # LONG -> FLAT : SELL
                    new[t + 1][0] = max(
                        new[t + 1][0],
                        dp[t][1] + price
                    )

                    new[t + 1][0] = max(
                        new[t + 1][0],
                        dp[t][2] - price
                    )
            dp = new
        return max(dp[t][0] for t in range(k + 1))