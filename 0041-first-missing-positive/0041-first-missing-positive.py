class Solution:
    def firstMissingPositive(self, arr: List[int]) -> int:
        i = 0
        while i < len(arr):
            correct = arr[i] - 1
            if 0 <= correct < len(arr) and arr[i] != arr[correct]:
                arr[i], arr[correct] = arr[correct], arr[i]
            else:
                i += 1
        for i in range(len(arr)):
            if i+1 != arr[i]:
                return i+1
        return len(arr) + 1