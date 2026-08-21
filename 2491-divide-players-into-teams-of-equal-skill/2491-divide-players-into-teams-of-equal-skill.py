class Solution:
    def dividePlayers(self, arr: List[int]) -> int:
        arr.sort()
        check = arr[0] + arr[-1]
        if len(arr) % 2 != 0:
            return -1
        ans = 0
        if len(arr) > 2:
            i = 1
            j = len(arr) - 2
            while i < j:
                if arr[i] + arr[j] != check:
                    return -1
                i += 1
                j -= 1
            i = 0
            j = len(arr) - 1
            while i < j:
                ans += arr[i]*arr[j]
                i += 1
                j -= 1
            return ans
        return arr[0] * arr[1]
        
