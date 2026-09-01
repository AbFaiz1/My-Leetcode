class Solution:
    def maxNumberOfAlloys(self, n: int, k: int, budget: int, compo: List[List[int]], stock: List[int], cost: List[int]) -> int:
        def feasible(mid, arr):
            price = 0
            for i in range(len(arr)):
                req = arr[i] * mid 
                diff = stock[i] - req
                if diff < 0:
                    price += abs(diff) * cost[i]
            if price <= budget:
                return True
            return False
        ans = 0
        for i in range(len(compo)):
            low = 0
            high = budget + max(stock)
            while low < high:
                mid = low + (high - low + 1)// 2
                if feasible(mid, compo[i]):
                    low = mid
                else:
                    high = mid - 1
            ans = max(ans, low)
        return ans
            