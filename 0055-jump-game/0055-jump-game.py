class Solution:
    def canJump(self, arr: List[int]) -> bool:
        reach = 0
        for i in range(len(arr)):
            if i > reach:
                return False
            if arr[i] + i > reach:
                reach = arr[i] + i
            if reach >= len(arr):
                return True
        return True