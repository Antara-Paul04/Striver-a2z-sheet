class Solution(object):
    def sortColors(self, nums):
        count_red, count_white, count_blue=0,0,0
        for i in nums:
            if i==0:
                count_red+=1
            elif i==1:
                count_white+=1
            else:
                count_blue+=1
        index=0        
        for j in range(count_red):
            nums[index] = 0
            index += 1
        for j in range(count_white):
            nums[index] = 1
            index += 1
        for j in range(count_blue):
            nums[index] = 2
            index += 1
        return nums
