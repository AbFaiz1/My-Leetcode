class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        timing = [0] * len(logs)
        timing[0] = logs[0][1]
        for i in range(1, len(logs)):
            timing[i] = logs[i][1] - logs[i-1][1]
        maxi = max(timing)
        ans = float("inf")
        for i in range(len(timing)):
            if timing[i] == maxi:
                ans = min(ans, logs[i][0])
        return ans
        