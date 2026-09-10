class Solution:
    def makesquare(self, arr: List[int]) -> bool:
        groups = [0] * 4
        target = sum(arr)
        if target % 4 != 0:
            return False
        target = target // 4
        def solve(i):
            if i >= len(arr):
                return True 
            for group in range(4):
                if group > 0 and groups[group] == groups[group-1]:
                    continue
                if groups[group] + arr[i] > target:
                    continue
                groups[group] += arr[i]
                if solve(i+1):
                    return True
                groups[group] -= arr[i]
            return False
        return solve(0)


