class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        map = {}
        def solve(i, j):
            if i >= len(s1):
                return sum(ord(ch) for ch in s2[j:])
            if j >= len(s2):
                return sum(ord(ch) for ch in s1[i:])
            if (i, j) in map:
                return map[(i, j)]
            if s1[i] == s2[j]:
                return solve(i+1, j+1)
            else:
                choice1 = ord(s1[i]) + solve(i+1, j)
                choice2 = ord(s2[j]) + solve(i, j+1)
                map[(i, j)] = min(choice1, choice2)
                return map[(i, j)]
        return solve(0, 0)