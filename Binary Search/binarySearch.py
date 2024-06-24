class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums)-1

        while (l<=r):
            mid = (l+r)//2
            key = nums[mid]
            if key == target:
                return mid
            elif target < key:
                r = mid-1
            else:
                l = mid+1
            
        return -1
