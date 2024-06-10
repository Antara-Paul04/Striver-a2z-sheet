class Solution(object):
    def merge(self, intervals):
        intervals.sort()
        ans=[]
        for i in range (len(intervals)):
            if not ans or intervals[i][0]>ans[-1][1]:
                ans.append(intervals[i])
            else:
                ans[-1][1]= max(intervals[i][1], ans[-1][1])
        return ans
