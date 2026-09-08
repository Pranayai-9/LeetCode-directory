class Solution:
    def smallestGoodBase(self, n):
        num = int(n)
        
        # The maximum possible number of bits/powers for n <= 10^18 is around 60
        max_m = num.bit_length() - 1
        
        # We loop from the largest possible exponent down to 2
        for m in range(max_m, 1, -1):
            # Binary search range for base k
            left = 2
            right = num
            
            while left <= right:
                mid = (left + right) // 2
                
                # Safely calculate the geometric sum: 1 + mid + mid^2 + ... + mid^m
                current_sum = 0
                for _ in range(m + 1):
                    current_sum = current_sum * mid + 1
                    # Early exit if the sum overshoots our target to prevent slow operations
                    if current_sum > num:
                        break
                
                if current_sum == num:
                    return str(mid)
                elif current_sum > num:
                    right = mid - 1
                else:
                    left = mid + 1
                    
        # Fallback case: n base (n - 1) is always "11"
        return str(num - 1)
