class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        current = []
        arrows = 0
        for point in points:
            if current and point[0] <= current[-1][1]:
                current[-1][1] = min(point[1], current[-1][1])
                continue
            elif current and point[0] > current[-1][1]:
                current.pop()
                current.append(point)
                arrows += 1
                continue
            elif not current:
                current.append(point)
        return arrows+1