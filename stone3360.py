class Solution:
    def canAliceWin(self, n):
        if 10 <= n <= 18:
            return True
        if 27 <= n <= 33:
            return True
        if 40 <= n <= 44:
            return True
        if 49 <= n <= 51:
            return True
        if n == 54:
            return True
            
        return False

