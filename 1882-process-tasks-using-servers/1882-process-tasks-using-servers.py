from heapq import heappop,heappush
class Solution:
    def assignTasks(self,servers:List[int],tasks:List[int])->List[int]:
        free=[]
        busy=[]
        ans=[0]*len(tasks)
        for i in range(len(servers)):
            heappush(free,(servers[i],i))
        for i in range(len(tasks)):
            while busy and busy[0][0]<i:
                end,w,idx=heappop(busy)
                heappush(free,(w,idx))
            if free:
                w,idx=heappop(free)
                ans[i]=idx
                end=i+tasks[i]-1
                heappush(busy,(end,w,idx))
            else:
                end,w,idx=heappop(busy)
                ans[i]=idx
                end=end+tasks[i]
                heappush(busy,(end,w,idx))

        return ans