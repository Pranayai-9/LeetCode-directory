class Solution:
    def isPowerOfTwo(self, n):
        # A power of two must be strictly greater than 0
        # n & (n - 1) must equal 0 to prove there is only one set bit
        return n > 0 and (n & (n - 1)) == 0
