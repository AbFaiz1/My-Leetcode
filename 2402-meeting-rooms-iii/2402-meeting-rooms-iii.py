import heapq

class Solution:
    def mostBooked(self, n, meetings):

        meetings.sort()

        free = list(range(n))
        heapq.heapify(free)

        busy = []

        count = [0] * n

        for start, end in meetings:

            # Jo rooms ab free ho gaye
            while busy and busy[0][0] <= start:
                finish, room = heapq.heappop(busy)
                heapq.heappush(free, room)

            # Agar room available hai
            if free:
                room = heapq.heappop(free)

                heapq.heappush(
                    busy,
                    (end, room)
                )

            # Sab rooms busy hain
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