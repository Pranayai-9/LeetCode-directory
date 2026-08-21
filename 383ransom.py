class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        for char in ransomNote:
            if char in magazine:
                # Remove only the first occurrence of the character
                magazine = magazine.replace(char, "", 1)
            else:
                return False
        return True

