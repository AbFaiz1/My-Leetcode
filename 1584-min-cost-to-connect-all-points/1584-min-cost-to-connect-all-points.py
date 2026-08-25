import heapq
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        heap = []
        heapq.heappush(heap, (0, 0))
        visited = set()
        ans = 0
        while heap:
            s, i = heapq.heappop(heap)
            if i in visited:
                continue
            visited.add(i)
            ans += s
            for j in range(len(points)):
                if j in visited:
                    continue
                a = abs(points[j][0] - points[i][0])
                b = abs(points[j][1] - points[i][1])
                dis = a + b
                heapq.heappush(heap, (dis, j))
        return ans
            