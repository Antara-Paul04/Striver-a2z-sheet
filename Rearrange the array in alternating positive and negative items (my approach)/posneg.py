class Solution(object):
    def rearrangeArray(self, nums):
        p_arr, n_arr = [], []
        for i in nums:
            if i >= 0:
                p_arr.append(i)
            else:
                n_arr.append(i)
                
        for i in range(len(nums) // 2):
            nums[2 * i] = p_arr[i]
            nums[2 * i + 1] = n_arr[i]
        
        return nums
