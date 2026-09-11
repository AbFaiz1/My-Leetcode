class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        prefix = []
        suffix = []

        prefix.append(arr[0])
        suffix.append(arr[-1])

        for i in range(1, len(arr)):
            if arr[i] < arr[i - 1]:
                break
            prefix.append(arr[i])

        if len(prefix) == len(arr):
            return 0

        for i in range(len(arr) - 2, -1, -1):
            if arr[i] > arr[i + 1]:
                break
            suffix.append(arr[i])

        suffix.reverse()

        ans = min(len(arr) - len(prefix), len(arr) - len(suffix))

        i = 0
        j = 0

        while i < len(prefix) and j < len(suffix):

            if prefix[i] <= suffix[j]:
                ans = min(ans, len(arr) - (i + 1) - (len(suffix) - j))
                i += 1
            else:
                j += 1

        return ans