class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        right = [0] * len(arr)
        left = [0] * len(arr)
        stack = []
        for i in range(len(arr) - 1, -1, -1):
            while stack and arr[i] <= arr[stack[-1]]:
                stack.pop()
            if not stack:
                right[i] = len(arr)
            else:
                right[i] = stack[-1]
            stack.append(i)
        stack = []
        for i in range(len(arr)):
            while stack and arr[i] < arr[stack[-1]]:
                stack.pop()
            if not stack:
                left[i] = -1
            else:
                left[i] = stack[-1]
            stack.append(i)
        ans = 0
        for i in range(len(arr)):
            left_count = i - left[i]
            right_count = right[i] - i
            ans += arr[i] * left_count * right_count
        return ans % (10**9 + 7)