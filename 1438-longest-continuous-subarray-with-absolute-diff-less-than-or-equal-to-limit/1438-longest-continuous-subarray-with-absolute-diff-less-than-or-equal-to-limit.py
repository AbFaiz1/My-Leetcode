from collections import deque
class Solution:
    def longestSubarray(self, arr: List[int], limit: int) -> int:
        dqmini = deque()
        dqmaxi = deque()
        def insertmini(val):
            while dqmini and val < dqmini[-1]:
                dqmini.pop()
            dqmini.append(val)
        def insertmaxi(val):
            while dqmaxi and val > dqmaxi[-1]:
                dqmaxi.pop()
            dqmaxi.append(val)
        left = 0
        right = 0
        ans = 0
        while right < len(arr):
            insertmini(arr[right])
            insertmaxi(arr[right])
            while left < len(arr) and dqmini and dqmaxi and abs(dqmini[0] - dqmaxi[0]) > limit:
                if arr[left] == dqmini[0]:
                    dqmini.popleft()
                if arr[left] == dqmaxi[0]:
                    dqmaxi.popleft()
                left += 1
            ans = max(ans, right-left+1)
            right += 1 
        return ans
