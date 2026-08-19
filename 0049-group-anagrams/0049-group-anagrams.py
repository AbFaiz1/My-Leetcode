class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = {}
        ans = []
        for str in strs:
            word = "".join(sorted(str))
            if word in mp:
                mp[word].append(str)
            else:
                mp[word] = []
                mp[word].append(str)
        for val in mp.values():
            ans.append(val)
        return ans