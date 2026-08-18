class Solution(object):
    def wordPattern(self, pattern, s):
        original = s.split()
        if len(pattern) != len(original):
            return False
        return len(set(pattern)) == len(set(original)) == len(set(zip(pattern, original)))

