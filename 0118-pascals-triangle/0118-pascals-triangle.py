class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = []
        ans.append([1])
        if numRows < 2:
            return ans
        ans.append([1,1])
        for i in range(3, numRows+1):
            temp = []
            temp.append(1)
            j = 1
            i = 0
            while j < len(ans[-1]):
                val1 = ans[-1][i]
                val2 = ans[-1][j]
                s = val1 + val2
                temp.append(s)
                i += 1
                j += 1
            temp.append(1)
            ans.append(temp)
        return ans