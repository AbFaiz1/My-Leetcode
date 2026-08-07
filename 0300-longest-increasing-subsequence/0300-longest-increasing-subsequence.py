class Solution:
    def lengthOfLIS(self, arr: List[int]) -> int:
        dp = [1] * len(arr)
        for i in range(len(arr)):
            maxi = 1
            for j in range(i-1, -1, -1):
                if arr[j] < arr[i]:
                    maxi = max(maxi, dp[j])
            dp[i] = maxi+1
        return max(dp)-1