class Solution:
    def findMedianSortedArrays(self, arr1: List[int], arr2: List[int]) -> float:
        arr = []
        i = 0
        j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                arr.append(arr1[i])
                i += 1
            else:
                arr.append(arr2[j])
                j+= 1
        arr.extend(arr1[i:])
        arr.extend(arr2[j:])
        n = len(arr)
        if n % 2 == 0:
            idx = n//2
            total = arr[idx] + arr[idx-1]
            avrg = total / 2
            return avrg
        else:
            return arr[n//2]
        

        