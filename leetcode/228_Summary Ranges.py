# medium

# Given a sorted integer array without duplicates, return the summary of its ranges.

# Example 1:

# Input:  [0,1,2,4,5,7]
# Output: ["0->2","4->5","7"]
# Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
# Example 2:

# Input:  [0,2,3,4,6,8,9]
# Output: ["0","2->4","6","8->9"]
# Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.


class Solution:
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        res = []
        l = len(nums)
        p = float('-inf')
        nums.append(p)
        temp = [p,p]
        for i in range(l):
            if nums[i] + 1 == nums[i+1]:
                if temp[1] == nums[i]:
                    temp.pop()
                    temp.append(nums[i+1])
                    res.pop()
                    res.append("{}->{}".format(temp[0],temp[1]))
                else:
                    res.append("{}->{}".format(nums[i],nums[i+1]))
                    temp = [nums[i],nums[i+1]]
            else:
                if temp[1] != nums[i]:
                    res.append(str(nums[i]))
        return res


t1 = [0,2,3,4,6,8,9]
t2 = [0,1,2,4,5,7]
t = Solution()
print(t.summaryRanges(t1))
print(t.summaryRanges(t2))