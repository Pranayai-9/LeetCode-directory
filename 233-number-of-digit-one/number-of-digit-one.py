class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        i = 1
        while i <= n:
            divider = i * 10
            # Compute full cycles of size divider
            count += (n // divider) * i
            # Compute remaining numbers in the incomplete cycle
            count += min(max(n % divider - i + 1, 0), i)
            i *= 10
        return count
