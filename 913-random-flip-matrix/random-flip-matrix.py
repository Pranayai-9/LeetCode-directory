import random


class Solution(object):

    def __init__(self, m, n):
        """ :type m: int

        :type n: int
        """
        self.m = m
        self.n = n
        self.total = m * n
        self.mapping = {}  # Tracks swapped indices

    def flip(self):
        """ :rtype: List[int] """
        # Decrement total first to get the last available boundary index
        self.total -= 1

        # Pick a random index from the remaining available slots
        idx = random.randint(0, self.total)

        # Check if this index was previously swapped, otherwise use its original value
        actual_idx = self.mapping.get(idx, idx)

        # The boundary element goes to the spot we just cleared out.
        # If the boundary element was already swapped, get its mapped destination.
        self.mapping[idx] = self.mapping.get(self.total, self.total)

        # Convert the 1D index back to 2D matrix coordinates
        return [actual_idx // self.n, actual_idx % self.n]

    def reset(self):
        """ :rtype: None """
        self.mapping.clear()
        self.total = self.m * self.n
