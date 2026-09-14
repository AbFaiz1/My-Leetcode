class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def solve(i, temp, dot):
            if dot == 3:
                last = s[i:]
                if not last:
                    return
                if len(last) > 1 and last[0] == '0':  
                    return
                elif int(last) > 255:
                    return
                ans.append(".".join(temp + [last]))  # FIX: last segment add
                return
            for j in range(i, i+3):
                if j < len(s):  
                    text = s[i:j+1]
                    if len(text) > 1 and text[0] == '0':  
                        continue
                    num = int(text)
                    if num > 255:
                        continue
                    temp.append(text)
                    dot += 1
                    solve(j + 1, temp, dot)  
                    dot -= 1
                    temp.pop()
        solve(0, [], 0)
        return ans