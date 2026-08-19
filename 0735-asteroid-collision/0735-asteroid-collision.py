class Solution:
    def asteroidCollision(self, arr: List[int]) -> List[int]:
        stack = []
        for i in range(len(arr)):
            if arr[i] < 0:
                while stack and stack[-1] > 0 and abs(stack[-1]) < abs(arr[i]):
                    stack.pop()
                if stack and stack[-1] > 0 and abs(stack[-1]) == abs(arr[i]):
                    stack.pop()
                    continue
                if len(stack) == 0:
                    stack.append(arr[i])
                    continue
                if stack and stack[-1] < 0:
                    stack.append(arr[i])
            else:
                stack.append(arr[i])
        return stack