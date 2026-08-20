import math

class Solution:
    def arrangeCoins(self, n):
        # Direct calculation using the quadratic formula
        return int((math.sqrt(8 * n + 1) - 1) // 2)
