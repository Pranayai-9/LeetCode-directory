class Solution(object):
    def getLeastFrequentDigit(self, n):
        num = list(str(n))
        frequency = []
        
        for digit in num:
            value = num.count(digit)
            frequency.append(value)
            
        ans = min(frequency)
        
        
        indices = [index for index, value in enumerate(frequency) if value == ans]
        tied_digits = [int(num[idx]) for idx in indices]
        
        return min(tied_digits) 

