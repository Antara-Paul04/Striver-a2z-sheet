class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0

        max_product = nums[0]
        curr_max = nums[0]
        curr_min = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < 0:
                curr_max, curr_min = curr_min, curr_max
            
            curr_max = max(nums[i], nums[i] * curr_max)
            curr_min = min(nums[i], nums[i] * curr_min)

            max_product = max(max_product, curr_max)

        return max_product
