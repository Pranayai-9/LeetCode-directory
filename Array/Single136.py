class Solution(object):
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))
            

#2.
class Solution(object):
    def containsDuplicate(self, nums):
        if len(nums) - len(set(nums)) != 0:
            return True
        else:
            return False
        

3.
class Solution(object):
    def containsDuplicate(self, nums):
        seen = set()
        for num in nums:
            if num in seen:
                return True # Found duplicate early, stop immediately
            seen.add(num)
        return False

