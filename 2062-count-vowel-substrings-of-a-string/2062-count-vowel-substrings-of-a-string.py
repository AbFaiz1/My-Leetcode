class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        def atmost(k):
            ans = 0
            mp = {}
            left = 0
            for i in range(len(word)):
                if word[i] not in vowels:
                    mp.clear()
                    left = i + 1
                    continue
                mp[word[i]] = mp.get(word[i], 0) + 1
                while len(mp) > k:
                    mp[word[left]] -= 1
                    if mp[word[left]] == 0:
                        del mp[word[left]]
                    left += 1
                ans += i - left + 1
            return ans
        return atmost(5) - atmost(4)
                
            