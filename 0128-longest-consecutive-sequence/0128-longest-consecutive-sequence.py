class Solution:
    def longestConsecutive(self, arr: List[int]) -> int:
        seen = set()
        for i in range(len(arr)):
            seen.add(arr[i])
        ans = float("-inf")
        if len(arr) == 0:
            return 0
        for i in range(len(arr)):
            count = 1
            right = 1 + arr[i]
            while right in seen:
                seen.remove(right)
                count += 1
                right += 1
            left = arr[i]-1
            while left in seen:
                seen.remove(left)
                count += 1
                left -= 1
            ans = max(ans, count)
        return ans
