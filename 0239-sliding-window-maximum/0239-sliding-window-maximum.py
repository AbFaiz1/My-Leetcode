from collections import deque
class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        ans = []
        dq = deque()
        for i in range(k):
            while dq and arr[i] > arr[dq[-1]]:
                dq.pop()
            dq.append((i))
        ans.append(arr[dq[0]])
        for i in range(k, len(arr)):
            if dq and dq[0] <= i - k:
                dq.popleft()
            while dq and arr[i] > arr[dq[-1]]:
                dq.pop()
            dq.append(i)
            ans.append(arr[dq[0]])
        return ans