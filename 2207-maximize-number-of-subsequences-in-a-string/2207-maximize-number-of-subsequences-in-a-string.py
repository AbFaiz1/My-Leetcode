class Solution:
    def maximumSubsequenceCount(self, arr: str, pattern: str) -> int:
        first = pattern[0]
        second = pattern[1]
        if first == second:
            count = arr.count(first)
            return (count + 1) * count // 2
        a = 0
        existing = 0
        count_a = 0
        count_b = 0
        for ch in arr:
            if ch == first:
                a += 1
                count_a += 1
            elif ch == second:
                existing += a
                count_b += 1
        return existing + max(count_a, count_b)