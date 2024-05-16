class Solution(object):
    def twoSum(self, nums, target):
        indices = []
        for i, num1 in enumerate(nums):
            complement = target - num1
            for j, num2 in enumerate(nums):
                if num2 == complement and j != i:
                    indices = [i, j]
                    return indices
