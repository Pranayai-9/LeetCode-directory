
class Solution(object):
    def mirrorDistance(self, n):
        num = str(n)
        rev = num[: :-1]
        diff = abs(int(rev)-int(num))
        return diff
        