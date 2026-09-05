class Solution:
    def maxFrequency(self, arr: List[int], k: int) -> int:
        ans = arr.count(k)
        for val in set(arr):
            temp = []
            if val == k:
                continue
            for v in arr:
                if v == k:
                    temp.append(-1)
                elif v == val:
                    temp.append(1)
                else:
                    temp.append(0)
            best = temp[0]
            curr = temp[0]
            for i in range(1, len(temp)):
                curr = max(temp[i], temp[i]+curr)
                best = max(curr, best)
            ans = max(ans, best + arr.count(k))
        return ans
            