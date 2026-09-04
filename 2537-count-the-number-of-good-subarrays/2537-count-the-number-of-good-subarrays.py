class Solution:
    def countGood(self, arr: List[int], k: int) -> int:
        mp = {}
        pairs = 0
        left = 0
        ans = 0
        for i in range(len(arr)):
            mp[arr[i]] = mp.get(arr[i], 0) + 1
            pairs += mp[arr[i]] - 1 
            while pairs >= k:
                ans += len(arr) - i
                mp[arr[left]] -= 1
                pairs -= mp[arr[left]]  
                left += 1
        return ans