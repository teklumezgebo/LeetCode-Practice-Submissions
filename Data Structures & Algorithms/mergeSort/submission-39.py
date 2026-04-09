# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def merge(self, pairs, s, m, e):
        L = pairs[s:m + 1] # Left side is start to middle
        R = pairs[m + 1:e + 1] # Right side is middle to end

        # index ptrs for L and R lists
        i = 0
        j = 0
        k = s # for pairs list, start at s arugement

        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                pairs[k] = L[i]
                i += 1
            else:
                pairs[k] = R[j]
                j += 1
            k += 1

        # Cleanup if one list is larger than the other

        while i < len(L):
            pairs[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            pairs[k] = R[j]
            j += 1
            k += 1

    def mergeSort(self, pairs: List[Pair], s=None, e=None) -> List[Pair]:
        if s is None and e is None:
            s, e = 0, len(pairs) - 1
            
        # base case: when the arr is of size 1 it is sorted
        if e - s + 1 <= 1:
            return pairs

        # middle index (start plus begining divide by 2)
        m = (s + e) // 2

        # 2 branch recursion, each branch takes has a half
        self.mergeSort(pairs, s, m)
        self.mergeSort(pairs, m + 1, e)

        self.merge(pairs, s, m, e)

        return pairs
