class Solution:
    def findMaxAverage(self, arr: List[int], k: int) -> float:
        currSum = sum(arr[:k])
        i = k
        ans = currSum  
        temp = 0
        j = 0

        while i < len(arr):
            currSum = currSum - arr[j] + arr[i]
            j += 1
            i += 1
            ans = max(ans, currSum)  

        return ans / k