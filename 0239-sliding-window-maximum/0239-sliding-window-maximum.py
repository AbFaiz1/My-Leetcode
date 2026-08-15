from collections import deque

class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        ans = []
        queue = deque()

        for i in range(k):
            while queue and queue[-1] < arr[i]:
                queue.pop()
            queue.append(arr[i])

        ans.append(queue[0])

        for i in range(k, len(arr)):

            if queue[0] == arr[i - k]:  
                queue.popleft()

            while queue and arr[i] > queue[-1]:
                queue.pop()

            queue.append(arr[i])

            ans.append(queue[0])

        return ans