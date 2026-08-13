class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()

        i = 0
        j = 0
        ans = 0

        while i < len(houses):

            while j + 1 < len(heaters) and heaters[j + 1] <= houses[i]:
                j += 1

            dist = abs(houses[i] - heaters[j])

            if j + 1 < len(heaters):
                dist = min(dist, abs(heaters[j + 1] - houses[i]))

            ans = max(ans, dist)

            i += 1

        return ans