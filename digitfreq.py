class Solution(object):
    def digitFrequencyScore(self, n):
        num = list(str(n))
        hh = list(set(num))
        arr = []
        value = 0
        for digit in hh:
           value = num.count(digit) * int(digit)
           arr.append(value)
           
        total = sum(arr)
        return total 




       
        
