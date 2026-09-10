class Solution:
    def findSubsequences(self, arr: List[int]) -> List[List[int]]:
        ans = []
        def solve(i, temp):
            if len(temp) >= 2:
                ans.append(temp.copy())
            for j in range(i + 1, len(arr)):
                if arr[j] < arr[i]:
                    continue
                temp.append(arr[j])  
                solve(j, temp)
                temp.pop()
        for i in range(len(arr)):  
            solve(i, [arr[i]])
        ans = list(set(map(tuple, ans)))
        return ans