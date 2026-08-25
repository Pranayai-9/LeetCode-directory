class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Set up three pointers pointing to the ends of the segments
        p1 = m - 1      # End of valid elements in nums1
        p2 = n - 1      # End of nums2
        p = m + n - 1   # Ultimate end of nums1 array
        
        # Merge elements from the back
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # If there are leftover elements in nums2, copy them over
        # (Leftover elements in nums1 are already in their correct places)
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1
