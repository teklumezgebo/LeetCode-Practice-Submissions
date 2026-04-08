class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        i = 0

        while i < len(nums2):
            nums1[m + i] = nums2[i]
            i += 1

        for i in range(1, len(nums1)):
            j = i - 1
            while j >= 0 and nums1[j] >= nums1[j + 1]:
                tmp = nums1[j]
                nums1[j] = nums1[j + 1]
                nums1[j + 1] = tmp
                j -= 1

        print(nums1)