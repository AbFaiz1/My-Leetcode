class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        ans = 0
        prev = 1
        for start, end in meetings:
            if start > prev:
                ans += start - prev
            prev = max(prev, end + 1)
        if prev <= days:
            ans += days - prev + 1
        return ans