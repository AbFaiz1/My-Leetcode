class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        n = len(arr)

        # 1. Pivot find karo
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1

        # 2. Agar pivot nahi mila, array descending hai
        if i == -1:
            arr.reverse()
            return

        # 3. Pivot se just bada element find karo
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1

        # 4. Swap
        arr[i], arr[j] = arr[j], arr[i]

        # 5. Pivot ke baad ka part reverse karo
        arr[i + 1:] = reversed(arr[i + 1:])