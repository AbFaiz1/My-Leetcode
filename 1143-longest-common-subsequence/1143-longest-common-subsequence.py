class Solution:
    def longestCommonSubsequence(self, arr1: str, arr2: str) -> int:
        map = {}
        def solve(i, j):
            if i >= len(arr1) or j >= len(arr2):
                return 0
            if (i, j) in map:
                return map[(i, j)]
            if arr1[i] == arr2[j]:
                map[(i, j)] = 1 + solve(i+1, j+1)
                return map[(i, j)]
            else:
                choice1 = solve(i+1, j)
                choice2 = solve(i, j+1)
                map[(i, j)] = max(choice1, choice2)
                return map[i, j]
        return solve(0,0)