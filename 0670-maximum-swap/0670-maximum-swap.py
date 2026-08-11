class Solution:
    def maximumSwap(self, num: int) -> int:
        ans = num
        s = list(str(num))

        for i in range(len(s)):
            for j in range(i + 1, len(s)):
                if s[j] > s[i]:
                    s[i], s[j] = s[j], s[i]

                    check = int(''.join(s))
                    ans = max(ans, check)

                    s[i], s[j] = s[j], s[i]

        return ans