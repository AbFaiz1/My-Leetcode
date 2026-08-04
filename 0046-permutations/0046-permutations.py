class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        visited = [False]*len(nums)
        def solve(temp):
            if len(temp) == len(nums):
                ans.append(temp[:])
                return
            for i in range(len(nums)):
                if visited[i]:
                    continue
                visited[i] = True
                temp.append(nums[i])
                solve(temp)
                temp.pop()
                visited[i] = False
        solve([])
        return ans