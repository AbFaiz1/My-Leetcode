class Solution:

    def restoreIpAddresses(self, s: str) -> List[str]:

        ans = []

        def solve(i, temp):

            if i == len(s):
                if len(temp) == 4:  # FIX: exactly 4 segments
                    ans.append(".".join(temp))
                return

            if len(temp) == 4:  # FIX: 4 segments ke baad stop
                return

            for j in range(i, i+3):

                if j < len(s):  # FIX: index boundary

                    text = s[i:j+1]

                    if len(text) > 1 and text[0] == '0':  
                        continue

                    num = int(text)

                    if num > 255:
                        continue

                    temp.append(text)

                    solve(j+1, temp)  

                    temp.pop()

        solve(0, [])

        return ans