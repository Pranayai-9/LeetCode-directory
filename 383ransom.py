class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for char in ransomNote:
            if char in magazine:
                # Remove only the first occurrence of the character
                magazine = magazine.replace(char, "", 1)
            else:
                return False
        return True

#O(1) space complexity using counters
from collections import Counter

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        # Subtracting counts clears keys that have a count <= 0
        return not (Counter(ransomNote) - Counter(magazine))

