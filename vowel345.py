#Two-pointer approach
class Solution(object):
    def reverseVowels(self, s):
        # 1. Convert to a list so we can modify characters in-place
        chars = list(s)
        
        # 2. Use a set for O(1) lightning-fast lookups
        vowels = set(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Move left pointer forward if it's not pointing to a vowel
            if chars[left] not in vowels:
                left += 1
                continue
                
            # Move right pointer backward if it's not pointing to a vowel
            if chars[right] not in vowels:
                right -= 1
                continue
            
            # Both pointers are on vowels, swap them!
            chars[left], chars[right] = chars[right], chars[left]
            
            # Move both pointers inward
            left += 1
            right -= 1
            
        # 3. Convert the list back into a string
        return "".join(chars)

