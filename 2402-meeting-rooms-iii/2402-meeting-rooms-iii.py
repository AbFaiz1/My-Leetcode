from heapq import heappush, heappop, heapify
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        free = list(range(n))
        heapify(free)
        pq = []
        rooms = [0] * n
        meetings.sort()
        for start, end in meetings:
            while pq and pq[0][0] <= start:
                e,r = heappop(pq)
                heappush(free, r)
            if free:
                heappush(pq, (end,free[0]))
                room = heappop(free)
                rooms[room] += 1
            else:
                e, r = heappop(pq)
                diff = end - start
                new = e + diff
                heappush(pq, (new, r))
                rooms[r] += 1
        temp = -1
        for i, val in enumerate(rooms):
            if val > temp:
                temp = val
                idx = i
        return idx
            


            