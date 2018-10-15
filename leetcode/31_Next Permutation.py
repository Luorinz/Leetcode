# medium

# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

# The replacement must be in-place and use only constant extra memory.

# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1




class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if nums == []:
            return 
        if len(nums) == 1:
            return 

        l = len(nums)
        res = []
        nums.reverse()
        is_find = False
        for i in range(1,l):
            if nums[i] < nums[i-1]:
                temp = nums[i]
                is_find = True
                for j in range(i):
                    if nums[j] > nums[i]:
                        nums[i] = nums[j]
                        nums[j] = temp
                        break          
                break
        if is_find:
            j = 0
            while j < i-1 :
                temp = nums[j]
                nums[j] = nums[i-1]
                nums[i-1] = temp
                i-=1
                j+=1

            nums.reverse()

        print(nums)
        

t = Solution()
print(t.nextPermutation([1,2,4,3,7,4,2]))
print(t.nextPermutation([1,2,3]))