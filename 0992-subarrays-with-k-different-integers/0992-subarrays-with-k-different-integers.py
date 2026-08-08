class Solution:
    def subarraysWithKDistinct(self, arr: List[int], k: int) -> int:
        mp = {}
        count = 0
        count2 = 0
        i = 0
        for j in range(len(arr)):
            mp[arr[j]] = mp.get(arr[j], 0)+1
            while len(mp) > k:
                mp[arr[i]] -= 1
                if mp[arr[i]] == 0:
                    del mp[arr[i]]
                i += 1
            count += j - i + 1
        mp = {}
        i = 0
        for j in range(len(arr)):
            mp[arr[j]] = mp.get(arr[j], 0)+1
            while len(mp) > k-1:
                mp[arr[i]] -= 1
                if mp[arr[i]] == 0:
                    del mp[arr[i]]
                i += 1
            count2 += j - i + 1 
        return count - count2