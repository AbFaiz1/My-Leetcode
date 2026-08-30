class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {}
        for i in range(len(s)-1, -1, -1):
            if s[i] in mp:
                continue
            mp[s[i]] = i
        ans = []
        left = 0
        best = 0
        for i in range(len(s)):
            if mp[s[i]] > best:
                best = mp[s[i]]
            if i == best:
                ans.append(i-left+1)
                left = i + 1
        return ans
