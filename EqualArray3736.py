#Brute-Force iterative incrementing
class Solution(object):
    def minMoves(self, nums):
        num = list(nums)
        target = max(num)
        if num.count(target) >= 2:
            while target in num:
                num.remove(target)
        else:
            num.remove(target)
        i=0
        count = 0
        while i < len(num) and num[i] != target:
            num[i] += 1
            count += 1
            if num[i] != target:
                continue
            else:
                i+=1
            
        return count



#Effecient approach: O(N) & O(1) Time and space complexity
class Solution(object):
    def minMoves(self, nums):
        # Find the target element (maximum) and total elements
        max_val = max(nums)
        n = len(nums)
        
        # Calculate moves using the total array sum
        return max_val * n - sum(nums)


class Solution(object):
    def minMoves(self, nums):
        # O(N) time to find the target, O(1) space
        target = max(nums)
        
        count = 0
        # O(N) time loop instead of an incrementing loop
        for num in nums:
            # Skip the target elements instead of removing them
            if num != target:
                # Math calculation replaces the one-by-one '+1' loop
                count += (target - num)
            
        return count

