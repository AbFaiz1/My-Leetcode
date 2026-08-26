class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        mp = {}
        for val in arr:
            mp[val] = mp.get(val, 0) + 1
        temp = []
        for k, v in mp.items():
            temp.append(v)
        temp.sort(reverse = True)
        total = sum(temp)
        goal = total // 2
        s = total
        ans = 0
        for i in range(len(temp)):
            s -= temp[i]
            ans += 1
            if s <= goal:
                return ans
        
    