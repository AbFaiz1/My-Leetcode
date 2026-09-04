from heapq import heappop, heappush
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        query = [(val,idx) for idx, val in enumerate(queries)]
        query.sort()
        pq = [] 
        ans = [-1] * len(query)
        j = 0
        for val, idx in query:
            while j < len(intervals) and intervals[j][0] <= val:
                heappush(pq, (intervals[j][1]-intervals[j][0] + 1, intervals[j][1]))
                j += 1
            while pq and pq[0][1] < val:
                heappop(pq)
            if pq:
                ans[idx] = pq[0][0]
        return ans
            
            