class Solution:
    def shipWithinDays(self, arr: List[int], days: int) -> int:
        low = max(arr)
        high = sum(arr)
        ans = float("inf")
        def feasible(mid):
            day = 1
            total = 0
            for i in range(len(arr)):
                total += arr[i]
                if total > mid:
                    day += 1
                    total = arr[i]
            if day <= days:
                return True
            return False
        while low <= high:
            mid = low + (high - low) // 2
            if feasible(mid):
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
        return ans
        