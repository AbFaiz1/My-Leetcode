class Solution:
    def consecutiveNumbersSum(self, n: int) -> int:
        def equation(n, k):
            return (2*n - (k-1)*k) / (2*k)
        count = 0
        for i in range(1, int((2*n)**0.5)+1):
            if equation(n, i) % 1 == 0:
                count += 1
        return count
                