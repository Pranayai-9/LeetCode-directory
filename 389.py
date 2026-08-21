class Solution(object):
    def findTheDifference(self, s, t):
        for char in set(t):
            if t.count(char) > s.count(char):
                return char

