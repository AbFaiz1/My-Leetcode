class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        bestAns = nums.count(k)
        for num in set(nums):
            if num == k:
                continue
            ans = []
            for val in nums:
                if val == k:
                    ans.append(-1)
                elif val == num:
                    ans.append(1)
                else:
                    ans.append(0)
            #kadanes Algorithm
            best = 0
            curr = 0
            for i in range(len(ans)):
                if curr < 0:
                    curr = 0
                curr += ans[i]
                best = max(best, curr)
            bestAns = max(bestAns, nums.count(k) + best)
        return bestAns
       