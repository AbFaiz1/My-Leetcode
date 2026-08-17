import heapq
class Solution:
    def minSumSquareDiff(self, arr1: List[int], arr2: List[int], k1: int, k2: int) -> int:
        heap = []
        n = len(arr1)
        for i in range(len(arr1)):
            heapq.heappush(heap, -(abs(arr1[i] - arr2[i])))
        k = k1 + k2
        while k > 0 and heap:
            decr = max(k//n, 1)
            val = -heapq.heappop(heap)
            if val == 0:
                continue
            val -= decr
            k -= decr
            if val < 0:
                heapq.heappush(heap, val)
                continue           
            heapq.heappush(heap, -val)
        ans = 0
        while len(heap) > 0:
            val = -heapq.heappop(heap)
            ans += val**2
        return ans
            
