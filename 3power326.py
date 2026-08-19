class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1



#Maximum int trick
class Solution(object):
    def isPowerOfThree(self, n):
        return n > 0 and 1162261467 % n == 0


#Logarithims
import math

class Solution(object):
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        res = math.log(n) / math.log(3)
        return abs(res - round(res)) < 1e-10
