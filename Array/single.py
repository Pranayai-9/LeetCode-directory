class Solution(object):
    def singleNumber(self, nums):
        for item in nums:
            if nums.count(item) == 1:
                return item
            else:
                continue
        

#Bitwise operation
class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for item in nums:
            result ^= item  # XOR operation
        return result

