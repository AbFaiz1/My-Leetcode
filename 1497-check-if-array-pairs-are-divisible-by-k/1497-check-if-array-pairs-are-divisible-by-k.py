class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        mp = {}
        count = 0
        if len(arr) % 2 != 0:
            return False
        for i in range(len(arr)):
            need = arr[i] % k
            if need in mp:
                count += 1
                mp[need] -= 1
                if mp[need] == 0:
                    del mp[need]
            else:
                store = (-arr[i]) % k
                mp[store] = mp.get(store, 0) + 1
        if count == len(arr) // 2:
            return True
        return False
            

            