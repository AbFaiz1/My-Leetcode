class Solution:
    def increasingTriplet(self, arr: List[int]) -> bool:
        mini = arr[0]
        maxi = arr[-1]
        left = [arr[0]] * len(arr)
        right = [arr[-1]] * len(arr)
        for i in range(len(arr)):
            if arr[i] <= mini:
                left[i] = mini
                mini = arr[i]
            else:
                left[i] = mini
        for i in range(len(arr)-1, -1, -1):
            if arr[i] >= maxi:
                right[i] = maxi
                maxi = arr[i]
            else:
                right[i] = maxi
        for i in range(1, len(arr)-1):
            if left[i] < arr[i] < right[i]:
                return True
        return False
                
                
                