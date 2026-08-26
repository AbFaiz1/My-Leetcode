class Solution:

    def maxProfit(self, k: int, arr: List[int]) -> int:

        buyLimit = k
        sellLimit = k
        mp = {}
        def solve(day, canBuy, canSell, buyLimit, sellLimit):

            if day == len(arr): 
                return 0

            if buyLimit <= 0:
                canBuy = False

            if sellLimit <= 0:
                canSell = False
            if (day, canBuy, canSell, buyLimit, sellLimit) in mp:
                return mp[(day, canBuy, canSell, buyLimit, sellLimit)]

            if canBuy:

                take = -arr[day] + solve(
                    day + 1,
                    False,
                    True,
                    buyLimit,
                    sellLimit
                ) 

                skip = solve(
                    day + 1,
                    True,
                    True,
                    buyLimit,
                    sellLimit
                ) 

                mp[(day, canBuy, canSell, buyLimit, sellLimit)] = max(take, skip) 
                return mp[(day, canBuy, canSell, buyLimit, sellLimit)]

            if canSell:

                take = arr[day] + solve(
                    day + 1,
                    True,
                    False,
                    buyLimit,
                    sellLimit - 1
                ) 

                skip = solve(
                    day + 1,
                    False,
                    True,
                    buyLimit,
                    sellLimit
                ) 

                mp[(day, canBuy, canSell, buyLimit, sellLimit)] = max(take, skip)
                return mp[(day, canBuy, canSell, buyLimit, sellLimit)]

            return 0 

        return solve(0, True, False, buyLimit, sellLimit)