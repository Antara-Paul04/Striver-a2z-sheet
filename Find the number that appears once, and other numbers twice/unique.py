class Solution(object):
    def singleNumber(self, nums):
        unique_num= 2* sum(set(nums))- sum(nums)
        return unique_num
