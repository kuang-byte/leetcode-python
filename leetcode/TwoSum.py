class Solution:
    @classmethod
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dict = {}
        for index, value in enumerate(nums):
            if target - value in dict:
                return index, dict[target -value]
            dict[value] = index 

print(Solution.twoSum([1,2,3], 5))
