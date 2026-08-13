class Solution(object):
    def sumAndMultiply(self, n):
        num = list(str(n))
        original = []
        for digit in num:
            if digit != str(0):
                original.append(int(digit))
            else:
                continue      
        if not original:
            return 0
        value = sum(original)
        final = int("".join(map(str,original)))
        ans = int(value) * final
        return ans


        
