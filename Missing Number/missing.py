class Solution(object):
    def missingNumber(self, nums):
        nums.sort()

        for i, num in enumerate(nums):
            if i != num:
                return i

        return len(nums)
