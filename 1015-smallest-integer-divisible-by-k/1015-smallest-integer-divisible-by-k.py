class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        val = 0
        for i in range(1, k+1):
            val = (val*10 + 1)
            if val % k == 0:
                return i
        return -1
            
            
