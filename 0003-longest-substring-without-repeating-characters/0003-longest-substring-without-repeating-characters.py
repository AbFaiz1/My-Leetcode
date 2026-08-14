class Solution:
    def lengthOfLongestSubstring(self, arr: str) -> int:
       left = 0
       window = set()
       best = 0
       for i in range(len(arr)):
            while arr[i] in window:
                window.remove(arr[left])
                left += 1
            window.add(arr[i])
            best = max(best, i - left + 1)
       return best
