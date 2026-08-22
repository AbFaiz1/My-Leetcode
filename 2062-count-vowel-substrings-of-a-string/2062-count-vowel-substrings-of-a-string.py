class Solution:
    def countVowelSubstrings(self, word: str) -> int:

        vowels = set("aeiou")

        def atMost(k):

            freq = {}
            left = 0
            ans = 0

            for right in range(len(word)):

                if word[right] not in vowels:
                    freq.clear()
                    left = right + 1
                    continue

                freq[word[right]] = freq.get(word[right], 0) + 1

                while len(freq) > k:
                    freq[word[left]] -= 1

                    if freq[word[left]] == 0:
                        del freq[word[left]]

                    left += 1

                ans += right - left + 1

            return ans

        return atMost(5) - atMost(4)