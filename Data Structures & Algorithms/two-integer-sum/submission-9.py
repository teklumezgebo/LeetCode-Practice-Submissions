class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumDict = {}
        sums = []

        for i in range(len(nums)):
            
            
            if target - nums[i] in sumDict:
                sums.append(sumDict[target - nums[i]])
                sums.append(i)
            else:
                sumDict[nums[i]] = i
             
        return sums