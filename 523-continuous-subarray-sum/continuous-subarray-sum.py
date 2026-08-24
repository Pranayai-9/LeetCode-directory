class Solution(object):

    def checkSubarraySum(self, nums, k):
        """ :type nums: List[int]

        :type k: int
        :rtype: bool
        """
        # Map to store {remainder: first_seen_index}
        # Initialized with 0 at index -1 to handle subarrays starting at index 0
        remainder_map = {0: -1}
        running_sum = 0

        for i, num in enumerate(nums):
            running_sum += num

            # Safeguard against k = 0 if required, though modern LeetCode guarantees k >= 1
            remainder = running_sum % k if k != 0 else running_sum

            if remainder in remainder_map:
                # Check if the length of the subarray is at least 2
                if i - remainder_map[remainder] >= 2:
                    return True
            else:
                # Only store the first time you see a remainder to maximize subarray length
                remainder_map[remainder] = i

        return False
