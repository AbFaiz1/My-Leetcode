class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        left = 0
        best =  1
        mini = float("inf")
        for i in range(len(s)):
            mp[s[i]] = mp.get(s[i], 0) + 1
            while (i - left + 1) - max(mp.values()) > k:
                mp[s[left]] -= 1
                if mp[s[left]] == 0:
                    del mp[s[left]]
                left += 1
            best = max(best, i - left + 1)
        return best
            