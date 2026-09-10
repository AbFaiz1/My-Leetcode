from functools import lru_cache
class Solution:
    def wiggleMaxLength(self, arr: List[int]) -> int:
        @lru_cache(None)
        def solve(i, pos, last):
            if i >= len(arr):
                return 0
            ans = 0
            for j in range(i+1, len(arr)):
                diff = arr[j] - last
                if diff == 0:
                    continue
                if pos and diff < 0:
                    continue
                if not pos and diff > 0:
                    continue
                if pos:
                    c = 1 + solve(j, False, arr[j])
                    ans = max(ans, c)
                if not pos:
                    c = 1 + solve(j, True, arr[j])
                    ans = max(ans, c)
            return ans
        ans = 1
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                diff = arr[j] - arr[i]
                if diff == 0:
                    continue  
                if diff > 0:
                    c1 = solve(j, False, arr[j])  
                    ans = max(ans, c1+2)  
                else:
                    c2 = solve(j, True, arr[j])  
                    ans = max(ans, c2+2)  
        return ans