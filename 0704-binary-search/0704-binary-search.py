class Solution:
    def search(self, arr: List[int], target: int) -> int:
        i, j = 0, len(arr)-1
        while i <= j:
            mid = (i + j) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                j = mid - 1
            else:
                i = mid + 1
        return -1