class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        sorted1 = "".join(sorted(s1))
        i, j = 1, len(s1)
        sorted2 = "".join(sorted(s2[:len(s1)]))
        if sorted2 == sorted1:
            return True
        while j < len(s2):
            sorted2 = "".join(sorted(s2[i:j + 1]))
            i += 1
            j += 1
            if sorted2 == sorted1:
                return True
        return False