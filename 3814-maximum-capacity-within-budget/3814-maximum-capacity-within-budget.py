class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        pairs = list(zip(costs, capacity))
        pairs.sort()

        costs = [p for p, c in pairs]
        capacity = [c for p, c in pairs]

        n = len(costs)

        # prefix[i] = top 2 capacities in 0...i
        prefix = []

        first = (-1, -1)
        second = (-1, -1)

        for i in range(n):
            cap = capacity[i]

            if cap > first[0]:
                second = first
                first = (cap, i)
            elif cap > second[0]:
                second = (cap, i)

            prefix.append((first, second))

        # Single machine
        ans = 0

        for i in range(n):
            if costs[i] < budget:
                ans = max(ans, capacity[i])

        i = 0
        j = n - 1

        while i < j:

            while i < j and costs[i] + costs[j] >= budget:
                j -= 1

            if i >= j:
                break

            first, second = prefix[j]

            # maximum capacity excluding i
            if first[1] != i:
                ans = max(ans, capacity[i] + first[0])
            else:
                ans = max(ans, capacity[i] + second[0])

            i += 1

        return ans