class Solution(object):
    def isSorted(self, arr):
        return arr == sorted(arr)

    def check(self, nums):
        min_val = min(nums)
        min_indices = [i for i, x in enumerate(nums) if x == min_val]
        n = len(nums) - 1

        if self.isSorted(nums) or any(self.isSorted(nums[:i]) and self.isSorted(nums[i:]) for i in min_indices) and nums[0] >= nums[n]:
            return True
        else:
            return False

nums = [3, 4, 5, 1, 2]
sol = Solution()
print(sol.check(nums))
