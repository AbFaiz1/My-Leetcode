class Fenwick:
    def __init__(self, n):
        self.bit = [0] * (n + 1)

    def update(self, i, delta):
        while i < len(self.bit):
            self.bit[i] += delta
            i += i & -i


    def query(self, i):
        total = 0
        while i > 0:
            total += self.bit[i]
            i -= i & -i
        return total

class Solution:
    def countSmaller(self, arr: List[int]) -> List[int]:
        values = sorted(set(arr))
        rank_map = {
            value: i + 1
            for i, value in enumerate(values)
        }


        compressed = [rank_map[val] for val in arr]
        fenwick = Fenwick(len(values))
        ans = [0] * len(arr)
        allRight = 0

        
        for i in range(len(compressed) - 1, -1, -1):
            ans[i] = fenwick.query(compressed[i]-1)
            fenwick.update(compressed[i], 1)
            allRight += 1
        return ans