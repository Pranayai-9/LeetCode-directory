#O(D^2)
class Solution(object):
    def maxProduct(self, n):
        num = list(str(n))
        x = [int(x) for x in num]
        product = []
        
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                value = int(num[i]) * int(num[j])
                product.append(value) 
                
        result  = max(product)
        return result 


#Sorting 
class Solution(object):
    def maxProduct(self, n):
        # Convert to list of integers
        digits = [int(d) for d in str(n)]
        
        # Edge case: If there's only 1 digit, you can't form a pair
        if len(digits) < 2:
            return 0  # Or handle as specified by the problem rules
        
        # Sort the digits in descending order
        digits.sort(reverse=True)
        
        # Multiply the two largest digits
        return digits[0] * digits[1]

#Linear optimization O(D):
class Solution(object):
    def maxProduct(self, n):
        # Edge case check for small numbers
        if n < 10:
            return 0 
            
        max1, max2 = -1, -1
        
        # Loop through each digit character directly without creating a list
        for char in str(n):
            digit = int(char)
            if digit > max1:
                max2 = max1
                max1 = digit
            elif digit > max2:
                max2 = digit
                
        return max1 * max2

