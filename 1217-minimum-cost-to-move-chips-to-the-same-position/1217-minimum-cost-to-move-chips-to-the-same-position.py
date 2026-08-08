class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odd = 0
        even = 0
        for pos in position:
            if pos % 2 == 0:
                even += 1
                continue
            odd += 1
        return min(even, odd)