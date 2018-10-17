# medium

# Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

# Example 1:

# Input: [[0, 30],[5, 10],[15, 20]]
# Output: 2
# Example 2:

# Input: [[7,10],[2,4]]
# Output: 1

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key = lambda x:x.start)

        end_list = []
        for interval in intervals:
            is_find = False
            for i in range(len(end_list)):
                if interval.start >= end_list[i]:
                    is_find = True
                    end_list[i] = interval.end
                    break
            if not is_find:
                end_list.append(interval.end)

        return len(end_list)