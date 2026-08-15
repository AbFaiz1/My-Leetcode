class Solution:
    def permute(self, arr: List[int]) -> List[List[int]]:
        visited = set()
        ans = []

        def solve(temp):
            if len(temp) == len(arr):  # FIX: complete permutation ban gayi
                ans.append(temp.copy())
                return

            for i in range(len(arr)):
                if i in visited:
                    continue

                visited.add(i)
                temp.append(arr[i])

                solve(temp)  

                temp.pop()        # FIX: backtrack
                visited.remove(i) # FIX: same element ko unvisit karo

        solve([])
        return ans