class Solution(object):
    def rearrangeArray(self, nums):
        array=[None]*len(nums)
        pos=0
        neg=1
        for i in nums:
            if i>=0:
                array[pos]=i
                pos+=2
            else:
                array[neg]=i
                neg+=2
        return array
        
