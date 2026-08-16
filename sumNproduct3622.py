class Solution(object):
    def checkDivisibility(self, n):
        num = str(n)
        value = 1
        for digit in num:
            value *= int(digit)
        ans = sum(int(digit) for digit in num) + value 
        if n % int(ans) == 0:
            return True
        else:
            return False 

        
        
