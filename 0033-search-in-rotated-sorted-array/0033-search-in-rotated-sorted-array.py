class Solution:
    def search(self, arr: List[int], target: int) -> int:
        i = 0
        j = len(arr) - 1
        while i <= j:
            mid = i + (j - i) // 2
            if arr[mid] == target:
                return mid
            if arr[i] <= arr[mid]:
                if arr[i] <= target < arr[mid]:
                    j = mid - 1
                else:
                    i = mid + 1
            else:
                if arr[mid] < target <= arr[j]:
                    i = mid + 1
                else:
                    j = mid - 1
        return -1