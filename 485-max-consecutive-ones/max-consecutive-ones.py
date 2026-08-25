class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_ones = 0      # Tracks the highest consecutive count seen so far
        current_ones = 0  # Tracks the current streak of 1s
        
        for num in nums:
            if num == 1:
                current_ones += 1
            else:
                # Streak broken by a 0: check if it's the max, then reset streak
                if current_ones > max_ones:
                    max_ones = current_ones
                current_ones = 0
                
        # Final check in case the array ends on a streak of 1s
        if current_ones > max_ones:
            max_ones = current_ones
            
        return max_ones
