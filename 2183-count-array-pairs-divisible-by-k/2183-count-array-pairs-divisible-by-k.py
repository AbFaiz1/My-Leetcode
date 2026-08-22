class Solution:
    def countPairs(self, arr, k):
        ans = 0
        mp = {}
        ans = 0
        for i in range(len(arr)):
            g = gcd(arr[i], k)
            need = k // g
            for key, freq in mp.items():
                if key % need == 0:
                    ans += freq
        
            mp[g] = mp.get(g, 0) + 1
        return ans

