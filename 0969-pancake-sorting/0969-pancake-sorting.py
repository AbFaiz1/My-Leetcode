from collections import deque

class Solution:

    def pancakeSort(self, arr: List[int]) -> List[int]:

        dq = deque()
        ans = []
        temp = sorted(arr)  # FIX: target sorted array hona chahiye

        for i in range(len(temp) - 1, -1, -1):
            dq.append(temp[i])

        count = 1

        while temp != arr:

            pos = arr.index(dq[0])

            if len(arr) - count == pos:
                count += 1
                dq.popleft()
                continue

            else:
                size = len(arr) - count + 1  # FIX: sirf unsorted prefix

                arr[:size] = arr[:size][::-1]  # FIX: full array nahi, unsorted prefix flip
                pos = arr.index(dq[0])
                ans.append(size)  # FIX: actual flip size

                if len(arr) - count == pos:
                    count += 1
                    dq.popleft()
                    continue

                else:
                    ans.append(pos + 1)

                    arr[:pos + 1] = arr[:pos + 1][::-1]
                    arr[:size] = arr[:size][::-1]  # FIX: target ko final position par bhejo
                    ans.append(size)

                    dq.popleft()
                    count += 1
                    continue

        return ans