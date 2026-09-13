class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        target = sum(arr)
        if target % k != 0:
            return False
        target = target // k
        groups = [0] * k
        arr.sort(reverse=True)
        def solve(i):
            if i >= len(arr):
                return True
            for group in range(k):
                if group > 0 and groups[group] == groups[group - 1]:
                    continue
                if groups[group] + arr[i] > target:
                    continue
                groups[group] += arr[i]
                if solve(i+1):
                    return True
                groups[group] -= arr[i] 
            return False
        return solve(0)
                
