class Solution:
    def perfectPairs(self, arr: List[int]) -> int:
        arr = [abs(x) for x in arr]
        arr.sort()
        count = 0
        def feasible(mid, i):
            if arr[mid] <= 2*arr[i]:
                return True
            return False
        for i in range(len(arr)-1):
            low = i
            high = len(arr) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if feasible(mid, i):
                    low = mid + 1
                else:
                    high = mid - 1
            count += (low - i - 1)
        return count
            