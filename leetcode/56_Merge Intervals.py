# Medium


# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considerred overlapping.



# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if intervals == []:
            return []
        l = len(intervals)
        if l == 1:
            return intervals
        res = []
        i = 1:
        while i < l:
            while intervals[i-1].end >= intervals[i].end:
                temp1 = intervals[i-1]
                i+=1
            res.append(temp1)
            while intervals[i-1].end >= intervals[i].start:
                temp2 =Interval(intervals[i-1].start,intervals[i].end)
                i+=1
            res.append()

            res.append(intervals[i-1])
            if i == l-1:
                res.append(intervals[i])
                


        return res
        
t1 = [[1,3],[2,6],[8,10],[15,18]]
t2 = [[1,4],[4,5]]
t = Solution()
print(t.merge(t1))
print(t.merge(t2))