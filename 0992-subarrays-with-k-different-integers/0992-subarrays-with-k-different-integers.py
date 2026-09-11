class Solution:
    def subarraysWithKDistinct(self, arr: List[int], k: int) -> int:
        def atmost(k):
            mp = {}  
            left = 0
            ans = 0
            for i in range(len(arr)):
                mp[arr[i]] = mp.get(arr[i], 0) + 1
                while len(mp) > k:
                    mp[arr[left]] -= 1
                    if mp[arr[left]] == 0:
                        del mp[arr[left]]
                    left += 1
                ans += i - left + 1
            return ans
        return atmost(k) - atmost(k - 1)