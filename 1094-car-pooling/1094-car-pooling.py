class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pairs = []
        for trip in trips:
            pairs.append((trip[1], 1, trip[0]))
            pairs.append((trip[2], -1, -trip[0]))
        pairs.sort()
        curr_capacity = 0
        for pair in pairs:
            curr_capacity += pair[2]
            if curr_capacity > capacity:
                return False
        return True