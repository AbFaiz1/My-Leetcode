class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6
        def dfs(nums):
            if len(nums) == 1:
                return abs(nums[0] - 24) < EPS
            n = len(nums)
            for i in range(n):
                for j in range(i + 1, n):
                    a = nums[i]
                    b = nums[j]
                    remaining = []
                    for k in range(n):
                        if k != i and k != j:
                            remaining.append(nums[k])
                    results = [
                        a + b,
                        a - b,
                        b - a,
                        a * b
                    ]
                    if abs(b) > EPS:
                        results.append(a / b)
                    if abs(a) > EPS:
                        results.append(b / a)
                    for value in results:
                        remaining.append(value)
                        if dfs(remaining):
                            return True
                        remaining.pop()
            return False
        return dfs(cards)