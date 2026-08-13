class Solution:
    def twoSum(self, arr: List[int], target: int) -> List[int]:
        i, j = 0, len(arr)-1
        while i < j:
            total = arr[i] + arr[j]
            if total == target:
                return [i+1, j+1]
            if total > target:
                j -= 1
            if total < target:
                i += 1
        