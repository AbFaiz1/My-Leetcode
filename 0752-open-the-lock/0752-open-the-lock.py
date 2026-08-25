from collections import deque
class Solution:
    def openLock(self, end: List[str], target: str) -> int:
        check = set(end)
        if target in check:
            return -1
        visited = set()
        dq = deque()
        word = "0000"
        dq.append((word, 0))
        while dq:
            word, ans = dq.popleft()
            if word == target:
                return ans
            if word in check:
                continue
            if word in visited:
                continue
            visited.add(word)
            for i in range(len(word)):
                digit = int(word[i])
                digit = (digit + 1) % 10
                digit = str(digit)
                new1 = word[:i] + digit + word[i+1:] 
                if new1 not in check:
                    dq.append((new1, ans+1))
                digit = int(word[i])
                digit = (digit - 1) % 10
                digit = str(digit)
                new2 = word[:i] + digit + word[i+1:]
                if new2 not in check:
                    dq.append((new2, ans+1)) 
        return -1
        

                