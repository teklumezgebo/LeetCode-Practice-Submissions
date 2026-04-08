class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        ptr = 0

        for i in range((2 * len(nums)) + 1):
            if ptr < len(nums):
                ans.append(nums[ptr])
                ptr += 1
            else:
                ptr = 0

        return ans
