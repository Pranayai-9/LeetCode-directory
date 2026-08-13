class Solution(object):
    def validDigit(self, n, x):
        num = str(n)
        if str(x) in num:
            if num.startswith(str(x)):
                return False 
            else:
                return True
        else:
            return False 
        
