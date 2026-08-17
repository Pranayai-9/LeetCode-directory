class Solution(object):
    def smallestIndex(self, nums):
        i = 0  
        while i < len(nums):
           digitList = []
           pop = list(str(nums[i]))
           for digit in pop:
            digitList.append(int(digit)) 
            if sum(digitList) == i:
                return i  
            else:
                i = i + 1  
                
       
        return -1

#O(N) & O(1) complexity:
class Solution(object):
    def smallestIndex(self, nums):
        # A single, clean for loop tracking index and value
        for i, num in enumerate(nums):
            digit_sum = 0
            
            # Extract digits mathematically without strings or lists
            while num > 0:
                digit_sum += num % 10  # Gets the last digit
                num //= 10             # Removes the last digit
            
            # Check the condition immediately
            if digit_sum == i:
                return i
                
        return -1

