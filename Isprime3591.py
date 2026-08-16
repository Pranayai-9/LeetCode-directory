from collections import Counter

class Solution(object):

    def is_prime(self, n):
        """Helper method to check if a single frequency is prime."""
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False  # Found a factor, so it is not prime
        return True  # No factors found, it is prime

    def checkPrimeFrequency(self, nums):
        # 1. Get frequencies of actual elements, not indices
        frequencies = Counter(nums).values()
        
        # 2. Check if ANY of the frequencies are prime
        for freq in frequencies:
            if self.is_prime(freq):
                return True # Found one prime frequency, we can stop early
                
        return False # Looked at all frequencies and found zero primes

