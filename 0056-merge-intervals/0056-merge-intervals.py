class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        current = []
        for interval in intervals:
            if current and interval[0] <= current[-1][1]:
                current[-1][1] = max(interval[1], current[-1][1])
                continue
            current.append(interval)
        return current

