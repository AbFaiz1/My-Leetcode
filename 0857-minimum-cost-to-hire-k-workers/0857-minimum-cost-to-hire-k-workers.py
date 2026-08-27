import heapq

class Solution:
    def mincostToHireWorkers(self, quality, wage, k):
        workers = []
        for q, w in zip(quality, wage):
            ratio = w / q
            workers.append((ratio, q))
        workers.sort()
        max_heap = []
        total_quality = 0
        answer = float('inf')
        for ratio, q in workers:

            heapq.heappush(max_heap, -q)
            total_quality += q

            if len(max_heap) > k:
                removed = -heapq.heappop(max_heap)
                total_quality -= removed

            if len(max_heap) == k:
                cost = total_quality * ratio
                answer = min(answer, cost)

        return answer