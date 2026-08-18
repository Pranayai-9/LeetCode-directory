class Solution(object):
    def findClosest(self, x, y, z):
        target = z
        val1 = abs(target - x)
        val2 = abs(target - y)
        if val1 < val2:
            return 1
        elif val1 > val2:
            return 2
        else:
            return 0
        
