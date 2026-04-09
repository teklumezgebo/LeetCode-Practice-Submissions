# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair], s=None, e=None) -> List[Pair]:
        if s is None:
            s, e = 0, len(pairs) - 1

        if e - s + 1 <= 1: # pair is of size 1, thus sorted
            return pairs

        # partition
        pivot = pairs[e]
        l = s

        for i in range(s, e):
            if pairs[i].key < pivot.key:
                tmp = pairs[l]
                pairs[l] = pairs[i]
                pairs[i] = tmp
                l += 1

        pairs[e] = pairs[l]
        pairs[l] = pivot

        
        self.quickSort(pairs, s, l - 1)
        self.quickSort(pairs, l + 1, e)

        return pairs
        