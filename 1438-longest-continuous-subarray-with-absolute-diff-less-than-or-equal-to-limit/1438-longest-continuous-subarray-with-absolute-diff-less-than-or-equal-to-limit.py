from collections import deque
class Solution:
    def longestSubarray(self, arr: List[int], limit: int) -> int:
        dqmini = deque()
        dqmaxi = deque()
        def insertmini(idx):
            while dqmini and arr[idx] < arr[dqmini[-1]]:
                dqmini.pop()
            dqmini.append(idx)  
        def insertmaxi(idx):
            while dqmaxi and arr[idx] > arr[dqmaxi[-1]]:
                dqmaxi.pop()
            dqmaxi.append(idx)  
        left = 0
        right = 0
        ans = 0
        while right < len(arr):
            insertmini(right)
            insertmaxi(right)
            while (arr[dqmaxi[0]] - arr[dqmini[0]]) > limit:
                if dqmini[0] == left:  
                    dqmini.popleft()
                if dqmaxi[0] == left:  
                    dqmaxi.popleft()
                left += 1
            ans = max(ans, right - left + 1)
            right += 1
        return ans