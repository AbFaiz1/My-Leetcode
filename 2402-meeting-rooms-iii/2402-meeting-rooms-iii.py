import heapq
class Solution:
    def mostBooked(self, n, meetings):

        meetings.sort()

        free = list(range(n))
        heapq.heapify(free)

        busy = []

        count = [0] * n

        for start, end in meetings:

            
            while busy and busy[0][0] <= start:
                finish, room = heapq.heappop(busy)
                heapq.heappush(free, room)

            
            if free:
                room = heapq.heappop(free)

                heapq.heappush(
                    busy,
                    (end, room)
                )

        
            else:
                finish, room = heapq.heappop(busy)

                duration = end - start

                newEnd = finish + duration

                heapq.heappush(
                    busy,
                    (newEnd, room)
                )

            count[room] += 1

        return count.index(max(count))