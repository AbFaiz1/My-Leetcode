class Solution:
    def reversePairs(self, arr: List[int]) -> int:
        ans = 0
        def merge_sort(arr):
            nonlocal ans
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left_arr = arr[:mid]
            right_arr = arr[mid:]
            left_sorted = merge_sort(left_arr)
            right_sorted = merge_sort(right_arr)
            return merge_arr(left_sorted, right_sorted)
        def merge_arr(left, right):
            nonlocal ans
            j = 0
            for i in range(len(left)):
                while j < len(right) and left[i] > 2 * right[j]:
                    j += 1
                ans += j
            i = 0
            j = 0
            temp = []
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    temp.append(left[i])
                    i += 1               
                else:
                    temp.append(right[j]) 
                    j += 1                 
            if left:
                temp.extend(left[i:])
            if right:
                temp.extend(right[j:])
            return temp                    
        merge_sort(arr)
        return ans