class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # left pointer l starts at index 1
        l = 1
        # right pointer also starts at 1
        for r in range(1, len(nums)):
            # check if index r and l are not equal
            if nums[r] != nums[r - 1]:
                # move current element to index l
                nums[l] = nums[r]
                l += 1
        # l is equal to the length of the unique array
        return l
        