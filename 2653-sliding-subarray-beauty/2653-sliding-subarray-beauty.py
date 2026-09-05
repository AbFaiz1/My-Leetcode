class Solution:
    def getSubarrayBeauty(self, arr: List[int], k: int, x: int) -> List[int]:
        offset = 50
        freq = [0] * 101
        for i in range(k):
            freq[arr[i] + offset] += 1
        count = 0
        ans = []
        for j in range(-50, 51):
            count += freq[j + offset]
            if count >= x:
                ans.append(min(j, 0))
                break
        left = 0
        for i in range(k, len(arr)):
            count = 0
            freq[arr[i] + offset] += 1
            freq[arr[left] + offset] -= 1
            left += 1
            for j in range(-50, 51):
                count += freq[j+offset]
                if count >= x:
                    ans.append(min(j, 0))
                    break
        return ans
