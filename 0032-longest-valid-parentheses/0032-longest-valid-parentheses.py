class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        maxLength = 0
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    maxLength = max(maxLength, i-stack[-1])
                else:
                    stack.append(i)
        return maxLength