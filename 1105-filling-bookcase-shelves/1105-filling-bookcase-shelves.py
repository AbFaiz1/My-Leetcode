from functools import lru_cache
class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        @lru_cache(None)
        def solve(i):
            if i >= len(books):
                return 0
            total = 0
            height = 0
            ans = float("inf")
            for j in range(i, len(books)):
                total += books[j][0]
                if total <= shelfWidth:
                    height = max(height, books[j][1])
                    c = height + solve(j+1)
                    ans = min(ans, c)
                else:
                    break
            return ans
        return solve(0)

