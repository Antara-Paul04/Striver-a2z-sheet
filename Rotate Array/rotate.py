class Solution(object):
    def rotate(self, nums, k):
        n=len(nums)
        k=k%n

        self.reverse(nums, 0, n-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, n-1)

    def reverse(self, nums, i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
sol = Solution()
result = sol.rotate(nums, k)
print(result)
