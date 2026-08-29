class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp = []
        for pair in pairs:
            if not dp:
                dp.append(pair)
            else:
                if dp[-1][1] < pair[0]:
                    dp.append(pair)
                else:
                    if dp[-1][1] > pair[1]:
                        dp.pop()
                        dp.append(pair)
        return len(dp)
        
