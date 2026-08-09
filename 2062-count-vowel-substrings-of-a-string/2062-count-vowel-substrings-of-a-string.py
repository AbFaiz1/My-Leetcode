class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        last = {v: -1 for v in vowels}
        last_consonant = -1
        count = 0
        for i, ch in enumerate(word):
            if ch not in vowels:
                last_consonant = i
            else:
                last[ch] = i

                if min(last.values()) > last_consonant:
                    count += min(last.values()) - last_consonant

        return count