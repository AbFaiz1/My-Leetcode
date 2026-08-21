class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        g1 = {2,3,4,5}
        g2 = {4,5,6,7}
        g3 = {6,7,8,9}
        mp = {}
        for temp in reservedSeats:
            if temp[0] not in mp:
                mp[temp[0]] = set()
            mp[temp[0]].add(temp[1])
        count = 0
        for reserved in mp.values():
            if not (reserved & g1):
                count += 1
                if not(reserved & g3):
                    count += 1
                continue
            else:
                if not (reserved & g2):
                    count += 1
                    continue
                if not (reserved & g3):
                    count += 1
                    continue
        return count + (n - len(mp))*2
