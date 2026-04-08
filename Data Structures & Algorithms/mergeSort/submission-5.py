# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, arr, s, m, e):
        L = arr[s: m + 1] # Left half of arr
        R = arr[m + 1: e + 1] # Right half of arr

        i = 0 # ptr for Left
        j = 0 # ptr for Right
        k = s # ptr for Arr

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

        return arr

    def mergeSort(self, arr: List[Pair], s=None, e=None) -> List[Pair]:
        if s is None: s = 0
        if e is None: e = len(arr) - 1
        if e - s + 1 <= 1:
            return arr
        
        m = (s + e) // 2
       
        self.mergeSort(arr, s, m)
        self.mergeSort(arr, m + 1, e)

        self.merge(arr, s, m, e)
        
        return arr
