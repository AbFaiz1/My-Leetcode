class Solution:
    def maxSubArray(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0] * n
        prefix[0] = arr[0]

        for i in range(1, n):
            prefix[i] = prefix[i-1] + arr[i]

        min_prefix = 0 
        ans = arr[0]

        for i in range(n):
            ans = max(ans, prefix[i] - min_prefix)  
            min_prefix = min(min_prefix, prefix[i]) 
        return ans