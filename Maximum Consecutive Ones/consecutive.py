class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_ones=0
        tsum=0
        for i in nums:
            if i==1:
                tsum+=1
                max_ones= max(max_ones,tsum)
            else:
                tsum=0
        return max_ones
