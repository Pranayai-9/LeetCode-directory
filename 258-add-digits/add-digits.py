class Solution:
    def addDigits(self, num):
       
        while num > 9:
            total = 0
            
            for digit in str(num):
                total += int(digit)
            
            num = total
            
        return num
