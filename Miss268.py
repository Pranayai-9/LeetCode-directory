#Brute force
class Solution(object):
    def missingNumber(self, nums):
        limit = len(nums)
        larry = []
        for i in range(limit + 1):
            larry.append(i)
        for f1 in larry:
            if f1 not in nums:
                return f1
            else:
                continue

#Difference approach
class Solution(object):
    def missingNumber(self, nums):
        value  = 0
        for i in range(len(nums)+1):
            value += 1
        return value - sum(nums)

#Gauss formula
class Solution(object):
    def missingNumber(self, nums):
        value  = (len(nums) * (len(nums) + 1))/2
        return value - sum(nums)