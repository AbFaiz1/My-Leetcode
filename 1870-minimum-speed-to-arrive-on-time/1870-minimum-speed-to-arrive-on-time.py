class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        i = 1
        j = 10**7
        def feasible(speed):
            time = 0
            for i in range(len(dist)):
                if i == len(dist) - 1:
                    time += dist[i] / speed
                    continue
                time += ceil(dist[i] / speed)
            if time <= hour:
                return True
            return False
        while i < j:
            speed = i + (j - i) // 2
            if feasible(speed):
                j = speed
            else:
                i = speed + 1
        if not feasible(i):
            return -1
        return i
