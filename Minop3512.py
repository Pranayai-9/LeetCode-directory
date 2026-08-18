class Solution(object):
    def minOperations(self, nums, k):
        op = 0
        if sum(nums) % k == 0:
            return 0
        else:
            for i in range(len(nums)):
                while nums[i] != 0:
                    nums[i] -=  1
                    op += 1
                    if sum(nums) % k == 0:
                        return op
                    else:
                        continue
            return op
       

#Direct return answer
class Solution(object):
    def minOperations(self, nums, k):
        return sum(nums) % k

