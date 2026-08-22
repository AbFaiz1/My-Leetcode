class Solution:
    def numberOfSubarrays(self, arr: List[int], k: int) -> int:
        mp = {}
        def atmost(k):
            left = 0
            ans = 0
            countodd = 0
            for i in range(len(arr)):
                if arr[i] % 2 != 0:
                    countodd += 1
                while countodd > k:
                    if arr[left] % 2 != 0:
                        countodd -= 1
                    left += 1
                ans += i - left + 1
            return ans
        return atmost(k) - atmost(k-1)
            