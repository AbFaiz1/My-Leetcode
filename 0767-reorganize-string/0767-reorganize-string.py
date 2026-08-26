from heapq import heappush, heappop
class Solution:
    def reorganizeString(self, s: str) -> str:
        mp = {}
        n = len(s)
        pq = []
        for i in range(n):
            mp[s[i]] = mp.get(s[i], 0)+1
        for key, val in mp.items():
            heappush(pq, (-val, key))
        i = 1
        ans = ""
        temp = ()
        while pq:
            val, node = heappop(pq)
            val = -val
            ans += node
            if temp:
                heappush(pq, (temp))
                temp = ()
                if val - 1 > 0:
                    val = val - 1
                    temp = (-val, node)
            else:
                if not pq:
                    val = val - 1
                    if val > 0:
                        heappush(pq, (-val, node))
                    
                if val - 1 > 0:
                    val = val - 1 
                    temp = (-val, node)
            if len(ans) >= 2:
                if ans[i] == ans[i-1]:
                    return ""
                i += 1
        return ans
            

